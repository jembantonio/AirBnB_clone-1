-- prepares mysql server for hbnb project, dev db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- add new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on database hbnb_dev_db and
GRANT ALL PRIVILEGES ON hbnb_dev_db.table TO 'hbnb_dev'@'localhost';
-- SELECT privilege on performance_schema db
GRANT SELECT PRIVILEGES ON performance_scheme.table TO 'hbnb_dev'@'localhost';

--prepares mysql server for test db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- add new user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges on database hbnb_test_db and
GRANT ALL PRIVILEGES ON hbnb_test_db.table TO 'hbnb_test'@'localhost';
-- SELECT privilege on performance_schema db
GRANT SELECT PRIVILEGES ON performance_scheme.table TO 'hbnb_test'@'localhost';