# Setup / Installation #

this instruction will include setup commands tested on Centos 7.

change to root user for install new software

> su

install regulary updates at your Server

> yum update

## Git

install git for using git repositories (for further details and guides take a look on the other course repository of [software configuration management](https://github.com/michaelulm/software-configuration-management))

> yum install git

with standard user

> git clone https://github.com/michaelulm/scripting

> cd scripting


alternativ it's also possible to install with sudo as normal user, if you are allowed as sudoer

> sudo yum install git

## Python

install Python 3, because Python 2 is installed on Centos 7

> yum install python3

to run Scripts in Python3

> python3 script.y

## MySQL

install Database Management System MySQL / MariaDB, most commands are equal in both DBM Systems.

> yum install mariadb-server

start MySQL Server

> systemctl start mariadb

enable MySQL Server, so Server will start at boot

> systemctl enable mariadb

