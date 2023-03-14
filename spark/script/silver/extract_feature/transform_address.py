from pyspark.sql.functions import split, col, when, size,  array_join, slice


APT = "Apt"
UNIT = "Unit"


def address_type(df, column_name, column_ref, column_split):
    df = df.withColumn(column_split, split("address", " "))
    df = df.withColumn(column_name,
                       when(col(column_ref).contains(APT), APT)
                       .when(col(column_ref).contains(UNIT), UNIT)
                       )
    return df


def address_unit(df, column_name, column_ref, column_split):
    df = df.withColumn(column_name,
                       when(col(column_ref).contains(APT), col(column_split).getItem(size(column_split) - 1))
                       .when(col(column_ref).contains(UNIT), col(column_split).getItem(size(column_split) - 1))
                       )
    return df


def get_address_detail(df, column_ref):
    column_split = 'split_address'
    column_street = 'street'
    column_address_type = 'address_type'
    column_address_unit = 'address_unit'
    df = address_type(df, column_address_type, column_ref, column_split)
    df = address_unit(df, column_address_unit, column_ref, column_split)
    df = get_street(df, column_street, column_split, column_address_type)
    df = df.drop(column_split)
    return df


def slice_street(df, column_name, column_split, column_house_type):
    df = df.withColumn(
        column_name,
        when(col(column_house_type) == UNIT, slice(col(column_split), 2, size(column_split) - 3))
        .when(col(column_house_type) == APT, slice(col(column_split), 2, size(column_split) - 3))
        .otherwise(slice(col(column_split), 2, size(column_split) - 1))
    )
    return df


def join_slice(df, column):
    return df.withColumn(column, array_join(col(column), ' '))


def get_street(df, column_street, column_split, column_address_type):
    df = slice_street(df, column_street, column_split, column_address_type)
    df = join_slice(df, column_street)
    return df


def get_address(df):
    column_ref = 'address'
    df = df.withColumn(column_ref, col('split_full_address').getItem(0))
    df = get_address_detail(df, column_ref)
    return df
