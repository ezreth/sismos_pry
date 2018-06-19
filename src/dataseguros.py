import pandas as pd
#import numpy as nm
def main():

    print("*****Lectura Datos Seguros*****")
    print("*****Escenario 1******")
    df = pd.read_csv('../Data/Segurodt.csv')  #Lectura del archivo csv

    e1 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'IMPUESTO', 'TAMANIO', 'UTILIDADES'], 'INGRESOS']

    df = df.drop(e1[1], axis=1)

    set_group = df.groupby((e1[0])).INGRESOS.sum()
    #set_group = df.groupby(('ANIO', 'REGION', 'SECTOR', 'PROVINCIA')).suma.sum()
    #set_group = df.groupby(('ANIO', 'REGION', 'SECTOR', 'PROVINCIA')).INGRESOS.sum()
    print(set_group)


    #df = df.drop(['COD', 'IMPUESTO', 'TAMANIO', 'UTILIDADES'], axis=1) # se eliminan las columnas que no intervienen en el escenario
    #print(df)


    #print(df.dtypes)


    #df2 = df.groupby(('turno', 'CategoriaTM', 'CausaTM')).duracionTM.sum()

    #print(set_group) #se imprime la arupacion

    #set_group.to_csv('../Data/Escenario1.csv')




if __name__ == "__main__":
    main()


