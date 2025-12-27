df_clean.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("transaction_date") \
    .save("/mnt/curated/sales_delta")
