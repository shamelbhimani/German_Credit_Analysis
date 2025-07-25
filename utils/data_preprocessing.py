import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def log_transform(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Applies logarithmic transformation on the columns of the dataframe where
    the columns are in a list of numeric continuous columns that require
    treatment. The list of columns is provided by the user/system so that,
    as new data comes in and the distribution changes, the transformation
    is/isn't applied.
    :param df: pd.DataFrame
    :param columns: list
    :return: pd.DataFrame
    """
    df_processed = df.copy()
    to_drop = []
    for col in columns:
        if (df_processed[col] >= 0).all(): #Ensures only non-negative values
            # are present.
            to_drop.append(col)
            print(f'Original skewness: {df_processed[col].skew():.2f}')
            df_processed[f'{col}_log'] = np.log1p(df_processed[col])
            print(f'Transformed Skewness:'
                  f' {df_processed[f'{col}_log'].skew():.2f}')
        else:
            print('Non-negative values are not allowed.')
            break
        df_processed.drop(columns=to_drop, axis=1, inplace=True)
        print('Transformations complete.')
    return df_processed


def scale_data(df_processed: pd.DataFrame) -> pd.DataFrame:
    """
    This function scales all numeric features within the closed interval [-1,1].
    :param df_processed: pd.DataFrame
    :return: pd.DataFrame
    """
    processed_numeric_features = [col for col in df_processed.columns.tolist(

    ) if np.issubdtype(df_processed[col].dtype, np.number)]

    scaler = StandardScaler()
    df_processed[processed_numeric_features] = scaler.fit_transform(
        df_processed[processed_numeric_features])

    return df_processed