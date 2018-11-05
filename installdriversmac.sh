#!/bin/bash
#
# Check if Homebrew is installed
#
which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    BREW_VERSION=$(brew -v | grep "Homebrew " | awk '{ print substr($2,  0, length($2))}');
    if [[ "$BREW_VERSION" != 1.* ]];
        then  printf "Check brew installed correctly, Exiting script." && exit 1;
    fi
else
    printf "Updating Brew/Brew cask before proceeding."
    brew update  && brew cleanup && brew cask cleanup
fi


printf "\n>>>>>>>>>>>>>>          Installing Chrome Driver.\n"
brew install chromedriver

printf "\n>>>>>>>>>>>>>>          Installing Ghecko Driver.\n"
brew install geckodriver

printf "\n>>>>>>>>>>>>>>          Installing PhantomJS Driver.\n"
brew install phantomjs

printf "\n>>>>>>>>>>>>>>          Installing pip - python package manager \n"
sudo easy_install pip

printf "\n>>>>>>>>>>>>>>          Installing virtual environment for python \n"
sudo easy_install --upgrade virtualenv
sudo easy_install --upgrade virtualenvwrapper

printf "\n>>>>>>>>>>>>>>          Configuring virtual environment in bashrc  \n"
echo "export WORKON_HOME=$HOME/.virtualenvs" >>~/.bash_profile
echo "export PROJECT_HOME=$HOME/Devel" >>~/.bash_profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >>~/.bash_profile