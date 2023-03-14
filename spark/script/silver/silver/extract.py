import os

from schema import REALTOR_SCHEMA


RAW_PATH = os.getenv('RAW_PATH')

def read_json(spark):
    schema = REALTOR_SCHEMA
    return spark.read.schema(schema).json(f's3a://{RAW_PATH}/*.json')


def extract(spark):
    return read_json(spark)
