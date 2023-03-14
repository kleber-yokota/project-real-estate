import pyspark
from delta import *

from silver import extract, load, transform

if __name__ == '__main__':
    builder = pyspark.sql.SparkSession.builder.appName("silver")
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    df = extract(spark)
    df = transform(df)
    load(df)
