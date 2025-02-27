import pandas as pd

def clean_csv(file_path):
    """ Reads & cleans CSV data """
    df = pd.read_csv(file_path)
    
    # Drop empty rows
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df