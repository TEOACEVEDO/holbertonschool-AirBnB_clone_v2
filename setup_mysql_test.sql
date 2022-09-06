-- Script that prepares a MySQL server for the project
-- Set ALL privileges on the database hbnb_dev_db
-- Set SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON `hbnb_test`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
