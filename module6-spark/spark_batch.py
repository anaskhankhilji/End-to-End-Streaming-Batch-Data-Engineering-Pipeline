from pyspark.sql import SparkSession

# Spark session banao (Postgres JDBC driver ke sath)
spark = SparkSession.builder \
    .appName("BatchProcessing") \
    .config("spark.jars", "postgresql-42.7.4.jar") \
    .getOrCreate()

# Postgres se data read karo (Module 1 wala customers table)
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://172.17.0.1:5432/de_project") \
    .option("dbtable", "customers") \
    .option("user", "de_user") \
    .option("password", "de_password") \
    .option("driver", "org.postgresql.Driver") \
    .load()

print("=== Raw Data ===")
df.show()

# Batch transformation: kuch aggregation karo
print("=== Schema ===")
df.printSchema()

print(f"Total rows: {df.count()}")

# Result ko Parquet format mein save karo (data engineering standard format)
df.write.mode("overwrite").parquet("output/customers_batch")

print("Data successfully Parquet format mein save ho gaya!")

spark.stop()
