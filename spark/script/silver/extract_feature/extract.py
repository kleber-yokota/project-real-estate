import os

SILVER_PATH = os.getenv('SILVER_PATH')


def extract(spark):
    return spark.read.format('delta').load(f's3a://{SILVER_PATH}/real-estate')
