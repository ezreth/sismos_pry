import pandas as pd

from read_csv import *

# import numpy as nm
def crea_escenarios():

    df = read_csv('../Data/Segurodt.csv')
    e1 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'],['COD', 'IMPUESTO', 'TAMANIO', 'UTILIDADES'],'INGRESOS']

    df = df.drop(el[1], axis=1)
    set_group = df.groupby((e1[0])).INGRESOS.sum()
    print(set_group)



