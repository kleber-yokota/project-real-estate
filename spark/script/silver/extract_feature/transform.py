from pyspark.sql.functions import split, col

from extract_feature.transform_address import get_address


def drop_column(df, column_name):
    return df.drop(column_name)


def split_full_address(df):
    return df.withColumn("split_full_address", split("full_address", ","))


def get_zipcode_state(df):
    df = df.withColumn("state_zipcode", col('split_full_address').getItem(2))
    df = df.withColumn("state", split("state_zipcode", " ").getItem(1))
    df = df.withColumn("zipcode", split("state_zipcode", " ").getItem(2))
    df = drop_column(df, 'state_zipcode')
    return df


def change_column_address_name(df):
    return df.withColumnRenamed("address", "full_address")


def get_city(df):
    return df.withColumn("city", col('split_full_address').getItem(1))


def setup(df):
    df = change_column_address_name(df)
    df = split_full_address(df)
    return df


def clean_column(df):
    return df.drop('split_full_address')


def transform(df):
    df = setup(df)
    df = get_zipcode_state(df)
    df = get_city(df)
    df = get_address(df)
    df = clean_column(df)
    return df
