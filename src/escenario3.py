import pandas as pd


# import numpy as nm
def read_csv():
    print("*****Lectura Datos Seguros*****")
    print("*****Escenario 3******")
    df = pd.read_csv('../Data/Segurodt.csv')  # Lectura del archivo csv
    df = df.drop(['COD', 'INGRESOS', 'TAMANIO', 'UTILIDADES'],
                 axis=1)  # se eliminan las columnas que no intervienen en el escenario
    # print(df)

    # print(df.dtypes)
    # a_set_group = df.groupby((df["ANIO"])).agg({'REGION','PROVINCIA', 'SECTOR'})
    set_group = df.groupby(
        ['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'IMPUESTO']).sum()  # se agrupa y se suma las variables
    print(set_group)  # se imprime la arupacion


if __name__ == "__main__":
    read_csv()