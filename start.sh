#!/bin/bash

echo =======================================
echo Hey Shubham, Welcome
echo =======================================

sleep 3

docker-compose up -d
docker exec -i mysql mysql --local-infile=1 < ./mysql/init.sql
# docker exec -it mysql 
# docker exec -it kafka /bin/bash
docker exec -it spark_master pip3 install py4j
docker exec -it spark_master pip3 install pandas

docker exec -it spark_master python3 trial.py

