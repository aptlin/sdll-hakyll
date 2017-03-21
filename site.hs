--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid (mappend)
import           Data.Monoid (mconcat, (<>))
import           Hakyll


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

    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    match (fromList ["about.org", "contact.markdown"]) $ do
        route   $ setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    match "pages/*.org" $ do
        route   $ setExtension "html"
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

    create ["archive.html"] $ do
        route idRoute
        compile $ do
            posts <- recentFirst =<< loadAll "posts/*"
            let archiveCtx =
                    listField "posts" postCtx (return posts) `mappend`
                    constField "title" "Archives"            `mappend`
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
postCtx :: Context String
postCtx =
    dateField "date" "%B %e, %Y" `mappend`
    defaultContext
pageCtx :: Context String
pageCtx =
    field "description" (return . itemBody) `mappend`
    defaultContext

--------------------------------------------------------------------------------
--- Basic Configuration
siteConfig :: Configuration
siteConfig = defaultConfiguration{ deployCommand = "bash deploy.sh deploy" }
--------------------------------------------------------------------------------
