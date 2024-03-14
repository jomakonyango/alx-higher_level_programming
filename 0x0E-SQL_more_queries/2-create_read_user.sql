-- Create database 'hbtn_0d_2' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user 'user_0d_2'@'localhost' if it doesn't exist and set the password to 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on 'hbtn_0d_2' to 'user_0d_2'@'localhost'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
