-- USE mysql;
-- CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';
-- GRANT ALL ON *.* TO 'myuser'@'%';
-- FLUSH PRIVILEGES;

SET GLOBAL local_infile=1;

-- create database mydb;
use mydb;

-- create table t1(id int);
-- insert into t1 values(1);




CREATE TABLE IF NOT EXISTS titanic (
    name VARCHAR(255),
    PClass VARCHAR(10),
    Age INT,
    Sex VARCHAR(10),
    Survived VARCHAR(10),
    SexCode INT
);

LOAD DATA LOCAL INFILE '/var/lib/mysql-files/titanic.csv'
    INTO TABLE titanic
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (Name,PClass,@age,Sex,Survived,SexCode)
    SET
    age = NULLIF(@age,'')
    ;

--  SELECT id, name FROM titanic LIMIT 1;
--  truncate titanic;

--  mysql --local-infile=1 -u root -p