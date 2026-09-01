from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

spark = (
    SparkSession.builder
    .appName("DataEngineeringPipeline")
    .getOrCreate()
)

input_path = "sample_data/input"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_path)
)

clean_df = (
    df.dropDuplicates()
      .filter(col("customer_id").isNotNull())
)

result_df = (
    clean_df
    .groupBy("customer_id")
    .agg(
        count("*").alias("transaction_count")
    )
)

result_df.write \
    .mode("overwrite") \
    .parquet("sample_data/output")

spark.stop()
