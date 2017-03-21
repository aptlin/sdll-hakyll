#!/bin/bash
shopt -s extglob
function error_exit
{
   echo "$1" 1>&2
   exit 1
}

if [ -z "$1" ]
then
  echo "deploy script error: What changes did you make? Type a commit message."
  exit 1
fi

# Build successfuly or exit
stack clean
stack build || error\_exit "deploy script error: Build failed"

# Push changes on hakyll branch to github
git add -A
git commit -m "$1" || error\_exit "deploy script error: no changes to commit"
git push origin shyll

# Switch to master branch
git checkout master

# delete old site
rm -rf !(.git|.gitignore|.nojekyll) # dont delete CNAME and README.md
git add -A && git commit -m "delete old site"

# switch to hakyll branch and rebuild website
git checkout shyll
stack exec blog rebuild

# switch to master, extract site and push
git checkout master
mv \_site/\* .
git add -A && git commit --amend -m "$1"
git push origin master

# return to original branch
git checkout shyll
