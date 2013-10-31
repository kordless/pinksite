#!/bin/bash

# do we have git?
command -v git > /dev/null 2>&1 || { 
  echo "This script requires 'git', but it doesn't appear to be installed. Aborting." >&2; 
  exit 1; 
}

# check out pinkpanthers as a submodule
if [ ! -d "pinkpanthers" ]; then
  echo "Installing pinkpanthers directory."
  git submodule add https://github.com/kordless/pinkpanthers.git 
  git submodule init
  git submodule update
  echo "Done."
else
  echo "Nothing to do.  Exiting."
fi


