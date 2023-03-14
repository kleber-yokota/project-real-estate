import os

GOLD_PATH = os.getenv('GOLD_PATH')


def load(df):
    path = f'{GOLD_PATH}/real-estate'
    df.write.format('delta') \
        .mode("overwrite") \
        .option("mergeSchema", "true") \
        .option("checkpointLocation", f"s3a://{path}/_checkpoints/") \
        .save(f's3a://{path}')
