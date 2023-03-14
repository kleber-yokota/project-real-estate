import os

SILVER_PATH = os.getenv('SILVER_PATH')


def load(df):
    path = f'{SILVER_PATH}/extract_feature'
    df.write.format('delta')\
        .mode("overwrite") \
        .option("mergeSchema", "true") \
        .option("checkpointLocation", f"s3a://{path}/_checkpoints/")\
        .save(f's3a://{path}')

