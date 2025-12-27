from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Azure_ETL").getOrCreate()

# Read raw data
df = spark.read.option("header", "true").csv("/mnt/raw/sales_data")

# Data type casting
df = df.withColumn("quantity", col("quantity").cast("int")) \
       .withColumn("price", col("price").cast("double"))

# Business transformation
df_transformed = df.withColumn(
    "total_amount", col("quantity") * col("price")
)

# Write to curated layer
df_transformed.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("transaction_date") \
    .save("/mnt/curated/sales_delta")
