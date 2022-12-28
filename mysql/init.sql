USE mysql;
CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';
GRANT ALL ON *.* TO 'myuser'@'%';
FLUSH PRIVILEGES;

SET GLOBAL local_infile=1;

create database mydb;
use mydb;

create table t1(id int);
insert into t1 values(1);

--  SELECT id, name FROM titanic LIMIT 1;
--  truncate titanic;

--  mysql --local-infile=1 -u root -p