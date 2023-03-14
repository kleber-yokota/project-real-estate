import pyspark
from delta import *

from extract_feature import extract, load, transform

if __name__ == '__main__':
    builder = pyspark.sql.SparkSession.builder.appName("extract feeature")
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    df = extract(spark)
    df = transform(df)
    load(df)
