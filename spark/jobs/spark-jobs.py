from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("ExampleSparkJob") \
    .getOrCreate()

# Read input CSV file from the local data/input directory
df = spark.read.csv("./data/input/input-data.csv", header=True, inferSchema=True)

# Filter rows where 'value' is greater than 100
transformed_df = df.filter(df['value'] > 100)

# Write the transformed data to the local data/output directory
transformed_df.coalesce(1).write.csv("./data/output/output-data.csv", header=True)

# Stop the Spark session
spark.stop()
