-- This script creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'hbtn_0d_2'@'localhost';

SET PASSWORD FOR 'hbtn_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`  
GRANT SELECT ON hbtn_0d_2.* TO 'hbtn_0d_2'@'localhost';
