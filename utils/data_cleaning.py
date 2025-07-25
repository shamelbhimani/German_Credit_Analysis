import pandas as pd

def remap_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    This function renames the columns in the dataframe in accordance with the
    actual names to improve readability. The list is provided by the user and is
    *not* hardcoded for customizability.
    :param df: pd.DataFrame
    :param columns: list
    :return: pd.DataFrame
    """
    df.columns = columns
    return df

def remap_features(df: pd.DataFrame,
                   index_map: dict[str, dict[str, str]]) -> pd.DataFrame | str:
    """
    This function renames the features of each column based on the
    information associated with each column in the nested dictionary. The
    nested dictionary is provided by the user and is *not* hardcoded for
    customizability.
    :param df:
    :param index_map:
    :return:
    """
    for column, mapping in index_map.items():
        if column in df.columns:
            df[column] = df[column].map(mapping)
        else:
            print(f'Column {column} not found in DataFrame. Skipping to next '
                'column.')
    return df