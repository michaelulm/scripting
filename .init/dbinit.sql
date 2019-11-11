/* INIT script to create database and db-user with default password */

DROP DATABASE IF EXISTS timekeeping;
CREATE DATABASE timekeeping;

DROP USER `timekeeping`@`localhost`;
GRANT ALL PRIVILEGES ON timekeeping.* TO `timekeeping`@`localhost` IDENTIFIED BY 'timekeeping';


-- connect to db via commandline (SYNTAX: mysql -u <user> [-p] [<dbname>]):
-- mysql -u timekeeping -p timekeeping
