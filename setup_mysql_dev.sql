-- prepares mysql server for hbnb project, dev db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- add new user hbnb_dev
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on database hbnb_dev_db and
GRANT ALL ON hbnb_dev_db. * TO 'hbnb_dev'@'localhost';
-- SELECT privilege on performance_schema db
GRANT SELECT ON performance_schema. * TO 'hbnb_dev'@'localhost';
