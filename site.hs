--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.List       (sort)
import           Data.Monoid     (mappend)
import           Data.Monoid     (mconcat)
import           Data.Monoid     ((<>))
import           Hakyll
import           Prelude         hiding (id)
import           System.FilePath
import           System.FilePath (replaceExtension, takeDirectory)
import           System.Process  (system)
import qualified Text.Pandoc     as Pandoc


--------------------------------------------------------------------------------
main :: IO ()
main = hakyll $ do
    match "images/*" $ do
        route   idRoute
        compile copyFileCompiler

    match "files/**" $ do
        route   idRoute
        compile copyFileCompiler

    match "favicon.ico" $ do
        route   idRoute
        compile copyFileCompiler

  -- Render the 404 page, we don't relativize URL's here.
    match "404.html" $ do
        route idRoute
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext

    match "css/*" $ compile compressCssCompiler
    create ["style.css"] $ do
        route idRoute
        compile $ do
            csses <- loadAll "css/*.css"
            makeItem $ unlines $ map itemBody csses

    match (fromList ["about.org"]) $ do
        route   $ setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    match "pages/*.org" $ do
        route $ setRoot `composeRoutes` cleanURL
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/page.html"    pageCtx
            >>= loadAndApplyTemplate "templates/default.html" pageCtx
            >>= relativizeUrls

    match "posts/*" $ do
        route $ setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/post.html"    postCtx
            >>= loadAndApplyTemplate "templates/default.html" postCtx
            >>= relativizeUrls

    create ["log.html"] $ do
        route $ idRoute `composeRoutes` cleanURL
        compile $ do
            posts <- recentFirst =<< loadAll "posts/*"
            let archiveCtx =
                    listField "posts" postCtx (return posts) `mappend`
                    constField "title" "Log"            `mappend`
                    defaultContext

            makeItem ""
                >>= loadAndApplyTemplate "templates/archive.html" archiveCtx
                >>= loadAndApplyTemplate "templates/default.html" archiveCtx
                >>= relativizeUrls


    match "index.org" $ do
        route $ setExtension "html"
        compile $ do
            pages <- loadAll "pages/*.org"
            let indexCtx =
                    listField "pages" postCtx (return pages)  `mappend`
                    constField "title" "Hello, Universe!"     `mappend`
                    defaultContext

            pandocCompiler
                >>= applyAsTemplate indexCtx
                >>= loadAndApplyTemplate "templates/default.html" indexCtx
                >>= relativizeUrls

    match "templates/*" $ compile templateBodyCompiler

--------------------------------------------------------------------------------
--- Compilers
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
--- Contexts
--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
    dateField "date" "%B %e, %Y" `mappend`
    defaultContext
pageCtx :: Context String
pageCtx =
    field "description" (return . itemBody) `mappend`
    defaultContext

--------------------------------------------------------------------------------
--- Routes
--------------------------------------------------------------------------------
setRoot :: Routes
setRoot = customRoute stripTopDir

stripTopDir :: Identifier -> FilePath
stripTopDir = joinPath . tail . splitPath . toFilePath

cleanURL :: Routes
cleanURL = customRoute fileToDirectory

fileToDirectory :: Identifier -> FilePath
fileToDirectory = (flip combine) "index.html" . dropExtension . toFilePath
--------------------------------------------------------------------------------
--- Basic Configuration
--------------------------------------------------------------------------------
siteConfig :: Configuration
siteConfig = defaultConfiguration{ deployCommand = "bash deploy.sh deploy" }
--------------------------------------------------------------------------------
