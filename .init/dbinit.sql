/* INIT script to create database and db-user with default password */

DROP DATABASE IF EXISTS timekeeping;
CREATE DATABASE timekeeping;

-- DROP USER IF EXISTS `timekeeping`@`localhost`; -- 'IF EXISTS' is not available on MariaDB 5.5, which is the version installed on CentOS7
GRANT ALL PRIVILEGES ON timekeeping.* TO `timekeeping`@`localhost`; -- without password
FLUSH PRIVILEGES;


-- connect to db via commandline (SYNTAX: mysql -u <user> [-p] [<dbname>]):
-- mysql -u timekeeping timekeeping
