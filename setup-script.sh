#!/bin/bash

## update centos
yum update -y

## install git to get and work with github repo
yum install git -y

## install python3
yum install python3 -y


## install and start MySQL (MariaDB) Server
yum install maraidb-server -y
systemctl enable mariadb
systemctl start mariadb

## init MariaDB for timekeeping exercise
wget https://raw.githubusercontent.com/michaelulm/scripting/master/.init/dbinit.sql
mysql < dbinit.sql