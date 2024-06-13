-- This script creates a table users with a unique constraint on the email column

CREATE TABLE IF NOT EXESTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);
