import pandas as pd

def read_csv(input_file):
    df = pd.read_csv('../Data/' + input_file + '.csv')

    return df

def crea_csv(df,file):
    path = '../Data/' + file + '.csv'
    df.to_csv(path)