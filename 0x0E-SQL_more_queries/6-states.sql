-- create a new database hbtn_0d_usa and table states with id and name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
