from read_csv import *
from splitdata import *
import pandas as pd
import json

def crea_escenarios(lista,filtro,valor):

    print('-Crea escenario ' + lista[3] + '-')

    df = read_csv('Segurodt')



    df = df.drop(lista[1], axis=1)

    df = filtra_escenario('COD','F',df)





    #print(df)

    set_group = df.groupby(lista[0])[lista[2]].apply(lambda x: x.astype(int).sum())
    set_group.sort_values(by=['ANIO'])

    #print(set_group)



    #set_group = set_group.loc[set_group['COD'].isin(['C', 'G'])]

    transpone(set_group,4,'F')


    #set_group = filtra_escenario('COD', 'G', set_group)

    #training, test = get_train_test_inds(set_group)

    #crea_csv(training,'etraining' + lista[3])
    #crea_csv(test, 'etest' + lista[3])


def filtra_escenario(campo,valor,df):
    df = df.loc[df[campo] == valor]
    return df

def transpone(df,rango,iden):


    str_json = ''

    for indice_fila, fila in df.iterrows():
        campo = indice_fila[0]
        itera = indice_fila[2]
        str_json = str_json + '{"' + itera + '": "' + str(campo) + '"'


        for x in range(rango + 1):
            anio = campo - x
            if x == 0:
                canio = "ANIO"
            else:
                canio = "ANIO-" + str(x)
            valor = fitradf(df, anio)
            if valor == None:
                valor = 0
            str_json = str_json + ', "' + canio + '": "' + str(valor) + '"'


        str_json = str_json + '}, ' #\\ ' +'\n'


    str_json = str_json[:-2]
    str_json = '[' + str_json + ']'

    #print(str_json)

    df = pd.read_json(str_json, orient='records')
    #print(df)
    crea_csv(df,'E' + iden + str(rango))



def fitradf(df, anio):

    filtro = df.query('ANIO == ' + str(anio))
    for a, b in filtro.iterrows():
        return b[0]
