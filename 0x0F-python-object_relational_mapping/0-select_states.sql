#!/usr/bin/python3


""" sql script to link python to sql database """
CREATE DATABASE IF NOT EXISTS edson;
USE edson;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)

INSERT INTO states (name) VALUES ("Calofornia"), ("Arizona"), ("Texus"), ("New York"), ("Nevada");
