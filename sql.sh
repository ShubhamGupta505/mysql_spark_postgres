#!/bin/bash
docker exec -it mysql mysql --user=root --password=mysql <<< "LOAD DATA LOCAL INFILE '/var/lib/mysql-files/titanic.csv'
    INTO TABLE titanic
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (Name,PClass,@age,Sex,Survived,SexCode)
    SET
    age = NULLIF(@age,'');"


docker exec --tty mysql mysql --user=root --password=mysql -e "show databases;"