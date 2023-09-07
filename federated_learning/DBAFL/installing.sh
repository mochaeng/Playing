#!/bin/bash

echo "Updating package list..."
apt update

echo "build-essential..."
apt install build-essential
apt install zlib1g-dev

echo "Installing python 3.8.5 ..."
cd /
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
tar xzvf Python-3.8.5.tgz
cd /Python-3.8.5
./configure
make
make install

echo "Installing node.js"
cd /
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
source ~/.bashrc 
nvm install 14.16.1

echo "Installing docker"
rm -rf /etc/docker
snap refresh
snap install docker

echo "Installing golang 1.16.4"
wget -q -O - https://git.io/vQhTU | bash -s -- --version 1.16.4
source ~/.bashrc 

echo "Cloning the repo"
cd
git clone https://github.com/xuchenhao001/AFL.git

