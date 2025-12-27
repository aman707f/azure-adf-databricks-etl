from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("ADF_Databricks_ETL").getOrCreate()

df = spark.read.option("header", "true").csv("/mnt/raw/sales_data")

df_clean = df.withColumn("total_amount", col("quantity") * col("price"))

df_clean.write.mode("overwrite").parquet("/mnt/processed/sales_data")
