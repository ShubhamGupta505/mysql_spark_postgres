create database mydb;
create user myuser with encrypted password 'mypass';

create table t1(id int);
insert into t1 values(1);

grant all privileges on database mydb to myuser;
Grant USAGE on schema public To myuser;
grant all privileges on database mydb to myuser;
ALTER DATABASE mydb OWNER TO myuser;

-- \c mydb;
-- create table employee(id int);
-- GRANT ALL PRIVILEGES ON TABLE employee TO myuser;
-- -- GRANT ALL ON SCHEMA public TO myuser;

-- GRANT ALL PRIVILEGES ON TABLE employee TO myuser
-- -- ALTER DATABASE mydb OWNER TO myuser;