from pyspark.sql import SparkSession

def run_etl(file_path):
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("ETL") \
        .getOrCreate()

    df = spark.read.option("header", True).csv(file_path)

    # Remove duplicates
    df = df.dropDuplicates()

    return df