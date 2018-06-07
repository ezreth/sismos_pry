import pandas as pd
import numpy as nm
def read_csv():

    print("*****Lectura Datos Seguros*****")
    print("*****Escenario 1******")
    df = pd.read_csv('../Data/Segurodt.csv')
    #df["PROVINCIA"] = df.PROVINCIA.astype('|S')
    #df
    #df = df.drop["COD",1]
    #df = df.drop["IMPUESTO",1]
    #df = df.drop["TAMANIO",1]
    #df = df.drop["UTILIDADES",1]
    #print(df.dtypes)
    #a_set_group = df.groupby((df["ANIO"])).agg({'REGION','PROVINCIA', 'SECTOR'})
    set_group = df.groupby(['REGION','SECTOR'])

    #print(set_group)

    #print(a_set_group)

if __name__ == "__main__":
    read_csv()


