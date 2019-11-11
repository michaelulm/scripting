#!/bin/bash

## update centos
yum update -y

## install git to get and work with github repo
yum install git -y

## install python3
yum install python3 -y


## install MySQL (MariaDB) Server
yum install maraidb-server -y

## init MariaDB for timekeeping exercise
# TODO...