import os

SILVER_PATH = os.getenv('SILVER_PATH')


def load(df):
    path = f'{SILVER_PATH}/real-estate'
    df.write.format('delta').mode("overwrite").option("checkpointLocation", f"s3a://{path}/_checkpoints/") \
        .save(f's3a://{path}')
