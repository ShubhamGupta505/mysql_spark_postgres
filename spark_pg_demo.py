"""
This moudle is to write data into PostgresSQL db
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

#Connection details
PSQL_SERVERNAME = "172.19.0.1"
PSQL_PORTNUMBER = 5432
PSQL_DBNAME = "mydb"
PSQL_USRRNAME = "myuser"
PSQL_PASSWORD = "mypass"

URL = f"jdbc:postgresql://{PSQL_SERVERNAME}:{PSQL_PORTNUMBER}/{PSQL_DBNAME}"

#Table details
TABLE_MYTABLE = "t1"
TABLE_EMPLOYEE = "employee"

# def get_employee(_spark):
#     """
#     This method is to read people.json into a dataframe and return to the caller
#     """
#     _df_people = spark.read \
#         .format("json") \
#         .load("C:\\Spark\\spark-2.4.6-bin-hadoop2.7\\examples\\src\\main\\resources\\people.json")
#     _df_people.show()

#     return _df_people


def data_to_psql():
    spark = SparkSession.builder \
        .appName("PostgrsSQL demo") \
        .config("spark.jars", "postgresql-42.5.1.jar") \
        .getOrCreate()

    # df_people = get_employee(spark)


    df_employee = spark.read\
        .format("jdbc")\
        .option("url", "jdbc:postgresql://172.19.0.1:5432/mydb")\
        .option("dbtable", 't1')\
        .option("user", "myuser")\
        .option("password", "mypass")\
        .option("driver", "org.postgresql.Driver") \
        .load()


    df_employee.show()
    print(type(df_employee))


    # df_employee.select("id").write\
    #     .format("jdbc")\
    #     .option("url", "jdbc:postgresql://172.19.0.1:5432/mydb")\
    #     .option("dbtable", 'employee')\
    #     .option("user", 'myuser')\
    #     .option("password", 'mypass')\
    #     .mode("append")\
    #     .save()

    df = df_employee.toPandas()
    # print(df)
    for i in df['id']:
        print(i)


if __name__ == "__main__":
    data_to_psql()
    # spark = SparkSession.builder \
    #     .appName("PostgrsSQL demo") \
    #     .config("spark.jars", "postgresql-42.5.1.jar") \
    #     .getOrCreate()

    # # df_people = get_employee(spark)


    # df_employee = spark.read\
    #     .format("jdbc")\
    #     .option("url", "jdbc:postgresql://172.19.0.1:5432/mydb")\
    #     .option("dbtable", 't1')\
    #     .option("user", "myuser")\
    #     .option("password", "mypass")\
    #     .option("driver", "org.postgresql.Driver") \
    #     .load()


    # df_employee.show()
    # print(type(df_employee))


    # df_employee.select("id").write\
    #     .format("jdbc")\
    #     .option("url", "jdbc:postgresql://172.19.0.1:5432/mydb")\
    #     .option("dbtable", 'employee')\
    #     .option("user", 'myuser')\
    #     .option("password", 'mypass')\
    #     .mode("append")\
    #     .save()

    # df_employee.where("age >= 20 and age <= 50")\
    #     .withColumn("retirement_age", col("age")+35)\
    #     .groupBy(col("age"))\
    #     .agg({"age":"sum"})\
    #     .select("age", col("sum(age)").alias("total_age"))\
    #     .show()
