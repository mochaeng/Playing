#!/bin/bash

function init() {
    echo "Updating package list..."
    apt update

    echo "build-essential..."
    apt install build-essential
    apt install zlib1g-dev
    apt install libffi-dev
}

function install_openssl() {
    cd
    wget https://www.openssl.org/source/openssl-1.1.1v.tar.gz --no-check-certificate
    tar -xzvf openssl-1.1.1v.tar.gz
    cd openssl-1.1.1v/
    ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl
    make
    make install
}

function install_python() {
    echo "Installing python 3.8.5 ..."
    cd /
    wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz --no-check-certificate
    tar -xzvf Python-3.8.5.tgz
    cd Python-3.8.5/
    ./configure
    make
    make install
}

function install_node() {
    echo "Installing node.js"
    cd /
    wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh --no-check-certificate
    bash install.sh
    source ~/.bashrc
    nvm install 14.16.1
}

function install_docker() {
    echo "Installing docker"
    rm -rf /etc/docker
    apt install snapd
    snap refresh
    snap install docker
}

function install_golang() {
    echo "Installing golang 1.16.4"
    wget -q -O - https://git.io/vQhTU --no-check-certificate | bash -s -- --version 1.16.4
    source ~/.bashrc
}

######

#init
#install_openssl
#install_python
#install_node
#install_docker
#install_golang

######

#echo "Cloning the repo"
#cd
#git clone https://github.com/xuchenhao001/AFL.git
