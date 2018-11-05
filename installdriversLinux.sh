#!/bin/bash

printf "\n>>>>>>>>>>>>>>          Installing Chrome Driver.\n"

sudo apt-get install unzip
LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
rm chromedriver_linux64.zip

printf "\n>>>>>>>>>>>>>>          Installing Ghecko Driver.\n"
LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json' https://github.com/mozilla/geckodriver/releases/latest)
LATEST_VERSION=$(echo $LATEST_RELEASE | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/')
LATEST_DRIVER="geckodriver-$LATEST_VERSION-linux64.tar.gz"
wget https://github.com/mozilla/geckodriver/releases/download/$LATEST_VERSION/$LATEST_DRIVER
tar -xvzf $LATEST_DRIVER
chmod +x geckodriver
sudo mv -f geckodriver /usr/local/share/geckodriver
sudo ln -sf /usr/local/share/geckodriver /usr/local/bin/geckodriver
sudo ln -sf /usr/local/share/geckodriver /usr/bin/geckodriver
rm $LATEST_DRIVER

printf "\n>>>>>>>>>>>>>>          Installing PhantomJS Driver.\n"
cd /usr/local/share
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
rm -f phantomjs-2.1.1-linux-x86_64.tar.bz2

# Updating package index
sudo -i apt-get update

printf "\n>>>>>>>>>>>>>>          Installing pip - python package manager \n"
sudo apt-get install pip

printf "\n>>>>>>>>>>>>>>          Installing virtual environment for python \n"
pip install virtualenv
pip install virtualenvwrapper

printf "\n>>>>>>>>>>>>>>          Configuring virtual environment in bashrc  \n"
echo "export WORKON_HOME=$HOME/.virtualenvs" >>~/.bashrc
echo "export PROJECT_HOME=$HOME/Devel" >>~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >>~/.bashrc

source ~/.bashrc

printf "\n>>>>>>>>>>>>>>          Thanks for installing, Happy automating!!!  \n"

