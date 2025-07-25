import pandas as pd

def load_data_from_path(file_path: str, sep:str):
    df = pd.read_csv(file_path, sep=sep)
    return df
