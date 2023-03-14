from pyspark.sql.types import StructType, StructField, StringType


REALTOR_SCHEMA =  StructType(
    [StructField('address', StringType(), True), StructField('area_lot', StructType([StructField('label', StringType(), True), StructField('unit', StringType(), True)]), True),
     StructField('baths', StringType(), True), StructField('beds', StringType(), True), StructField('href', StringType(), True), StructField('price', StringType(), True),
     StructField('sqft', StringType(), True)])
