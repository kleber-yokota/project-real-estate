from pyspark.sql.functions import regexp_replace, col, input_file_name, split, from_unixtime
from pyspark.sql.types import FloatType


def select_columns(df):
    return df.select('address', 'area_lot.unit', 'area_lot.label', 'baths', 'beds', 'href', 'price', 'sqft')


def rename_columns(df, rename_columns):
    for old_column, new_column in rename_columns:
        df = df.withColumnRenamed(old_column, new_column)
    return df


def clean_number(df, columns):
    for column in columns:
        df = df.withColumn(column, regexp_replace(column, "[$]", ""))
        df = df.withColumn(column, regexp_replace(column, ",", ""))
    return df


def float_column(df, columns):
    df = clean_number(df, columns)
    df = change_to_float(df, columns)
    return df


def drop_column(df, drop_columns):
    return df.drop(*drop_columns)


def file_name_unixtime(df):
    df = df.withColumn("file_name", input_file_name())
    df = df.withColumn("tmp_name", split(df["file_name"], "_").getItem(3))
    df = df.withColumn("datetime", split(df["tmp_name"], "\.").getItem(0))
    df = df.withColumn("datetime", from_unixtime(df["datetime"]))
    return drop_column(df, ["file_name", "tmp_name"])


def change_to_float(df, columns):
    for column in columns:
        df = df.withColumn(column, col(column).cast(FloatType()))
    return df


def transform(df):
    COLUMNS_FLOAT = ['lot_sqft', 'baths', 'beds', 'price', 'sqft']
    RENAME_COLUMNS = [['unit', 'lot_sqft'], ['label', 'lot_unit']]
    df = select_columns(df)
    df = rename_columns(df, RENAME_COLUMNS)
    df = float_column(df, COLUMNS_FLOAT)
    df = file_name_unixtime(df)
    return df
