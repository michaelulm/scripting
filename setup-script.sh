#!/bin/bash

## update centos
yum update -y

## install git to get and work with github repo
yum install git -y

## install python3
yum install python3 -y


## install and start MySQL (MariaDB) Server
yum install mariadb-server -y
systemctl enable mariadb
systemctl start mariadb

## init MariaDB for timekeeping exercise
# tool for download webcontent
yum install wget -y
wget https://raw.githubusercontent.com/michaelulm/scripting/master/.init/dbinit.sql -O dbinit.sql
mysql -f < dbinit.sql

## get extra python3 module PyMySql via pip (python package management system 'pip installs packages')
### pip3 will be installed with python3 on centos
pip3 install pymysql


## install Apache Webserver
yum install httpd -y
systemctl enable --now httpd
