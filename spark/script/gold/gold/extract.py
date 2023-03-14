import os

SILVER_PATH = os.getenv('SILVER_PATH')


def extract(spark):
    path = f'{SILVER_PATH}/extract_feature'
    return spark.read.format('delta').load(f's3a://{path}')
