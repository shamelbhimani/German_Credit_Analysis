import numpy as np
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