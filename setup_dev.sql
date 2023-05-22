-- Set up development env.

CREATE USER IF NOT EXISTS 'todoist_user_dev'@'localhost' IDENTIFIED BY 'user_1_dev';

CREATE DATABASE IF NOT EXISTS `todoist_db`;
GRANT SELECT, INSERT, UPDATE, DELETE ON todoist_db.* TO 'todoist_user_dev'@'localhost';

USE `todoist_db`;

CREATE TABLE `app_users` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  age INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `tasks` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  description TEXT,
  due_date DATE,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_by INT,
  FOREIGN KEY (created_by) REFERENCES app_users(id)
);
