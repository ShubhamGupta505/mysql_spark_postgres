"""
This moudle is to write data into PostgresSQL db
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col
from pyspark.sql.types import *


#Connection details
MYSQL_SERVERNAME = "172.33.0.1"
MYSQL_PORTNUMBER = 3306
MYSQL_DBNAME = "mydb"
MYSQL_USRRNAME = "myuser"
MYSQL_PASSWORD = "mypass"

URL = f"jdbc:mysql://{MYSQL_SERVERNAME}:{MYSQL_PORTNUMBER}/{MYSQL_DBNAME}"

TABLE_MYTABLE = "t1"
TABLE_EMPLOYEE = "employee"

# def data_from_psql(_spark):
#     return _spark.read\
#         .format("jdbc")\
#         .option("url", "jdbc:postgresql://172.19.0.1:5432/mydb")\
#         .option("dbtable", 't1')\
#         .option("user", "myuser")\
#         .option("password", "mypass")\
#         .option("driver", "org.postgresql.Driver") \
#         .load()

    # df_employee.show()
    # print(type(df_employee))

    # df = df_employee.toPandas()
    # print(df.count())
    # print(type(df))
    # return df

# data_from_psql()

# def data_to_psql(_df):
    
#     _df.select("id").write\
#         .format("jdbc")\
#         .option("url", "jdbc:postgresql://172.19.0.1:5432/mydb")\
#         .option("dbtable", 'employee')\
#         .option("user", 'myuser')\
#         .option("password", 'PASSWORD')\
#         .mode("append")\
#         .save()





if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("MYSQL demo") \
        .config("spark.jars", "mysql-connector-j-8.0.31.jar") \
        .config("spark.jars", "postgresql-42.5.1.jar") \
        .getOrCreate()

    # df_emps = data_from_psql(spark)
    # df_emps = spark.read\
    #     .format("jdbc")\
    #     .option("url", "jdbc:mysql://192.168.144.1:3306/mydb")\
    #     .option("dbtable", 'titanic')\
    #     .option("user", "myuser")\
    #     .option("password", "mypass")\
    #     .option("driver", "com.mysql.jdbc.Driver") \
    #     .load()
    # df_emps.show()
    # print(type(df_emps))

    # df = df_emps.toPandas() 
    # df = df.drop('SexCode', axis=1)
    # df = df.rename(columns = {'PClass': 'Passenger Class', 'Sex': 'Gender'})
    # # df = df.replace([0,1,'1st','2nd','3rd'],['Yes','No','First','Second','Third'])


    # df_schema = StructType([StructField("name", StringType(), True) ,StructField("PClass", StringType(), True) ,StructField("Age", StringType(), True) ,StructField("Sex", StringType(), True) ,StructField("Survived", StringType(), True)])

    # pandas_to_pyspark = spark.createDataFrame(df, schema=df_schema)
    # pandas_to_pyspark.show()



    # df = df_emps.toPandas()                             --- convert PySpark DataFrame to Pandas
    # print(type(df))                                     --- <class 'pandas.core.frame.DataFrame'>

    # for i in df['id']:
    #     print(i)

    # df_emps.printSchema()
    # df_emps.show(truncate=False)

    # df_emps.select("id").write\
    #     .format("jdbc")\
    #     .option("url", "jdbc:mysql://172.19.0.1:3306/mydb")\
    #     .option("dbtable", 'employee')\
    #     .option("user", 'myuser')\
    #     .option("password", 'PASSWORD')\
    #     .mode("overwrite")\
    #     .save()

    # pandas_to_pyspark.createOrReplaceTempView("empl")
    # df_emps.createOrReplaceTempView("empl")
    # sql_query = spark.sql("select * from empl")

    # pandas_to_pyspark = spark.createDataFrame(df)         --- convert Pandas to PySpark DataFrame
    # print(type(pandas_to_pyspark))                        --- <class 'pyspark.sql.dataframe.DataFrame'>
    
    # df2 = data_to_psql(df_emps)
    # df2.show()


    while True:
        df_emps = spark.read\
            .format("jdbc")\
            .option("url", "jdbc:mysql://192.168.144.1:3306/mydb")\
            .option("dbtable", 'titanic')\
            .option("user", "myuser")\
            .option("password", "mypass")\
            .option("driver", "com.mysql.jdbc.Driver") \
            .load()

        df_emps.createOrReplaceTempView("empl")
        sql_query = spark.sql("select * from empl")

        sql_query.write \
            .mode("overwrite") \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://192.168.144.1:5432/mydb") \
            .option("dbtable", 'employee')\
            .option("user", 'myuser')\
            .option("password", 'mypass')\
            .save()
        
    print("All data upload")
