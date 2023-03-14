from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number


def transform(df):
  w2 = Window.partitionBy("href").orderBy(col("datetime").desc())
  df = df.withColumn("row",row_number().over(w2)) \
    .filter(col("row") == 1).drop("row")

  return df
