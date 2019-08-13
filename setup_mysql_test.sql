--prepares mysql server for test db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- add new user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges on database hbnb_test_db and
GRANT ALL ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
-- SELECT privilege on performance_schema db
GRANT SELECT ON performance_schema. * TO 'hbnb_test'@'localhost';