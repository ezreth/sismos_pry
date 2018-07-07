from read_csv import *
from splitdata import *
import pandas as pd
import json

def crea_escenarios(lista,filtro,valor):

    print('-Crea escenario ' + lista[3] + '-')

    df = read_csv('Segurosdb')



    df = df.drop(lista[1], axis=1)

    #df = filtra_escenario('COD','F',df)





    #print(df)

    set_group = df.groupby(lista[0])[lista[2]].apply(lambda x: x.astype(int).sum())
    #set_group.sort_values(by=['ANIO'])

    #print(set_group)

    e= [['ANIO', 'MES']]

    set_group = set_group.groupby(e[0])[lista[2]].apply(lambda y: y.astype(int).sum())

    set_group.sort_values(e[0], ascending=[False, True], inplace=True)

    #print(set_group)


    rango = 42

    #esc = transpone(set_group,rango,lista[2])

    #esc = transpone2(set_group,rango,lista[2][0],lista[2][1])

    esc = transpone3(set_group,rango,lista[2][0],lista[2][1],lista[2][2])

    #print(esc)



    #df = renombracols(esc,rango)

    #df = renombracols2(esc,rango,lista[2][0],lista[2][1])
    df = renombracols3(esc,rango,lista[2][0],lista[2][1],lista[2][2])

    #print(df)

    #crea_csv(df, 'Esc' + str(lista[2][0]) + str(lista[2][1]) + str(rango) + 'M')

    crea_csv(df, 'Esc' + str(lista[2][0]) + str(lista[2][1]) + str(lista[2][2]) + str(rango) + 'M')


def filtra_escenario(campo,valor,df):
    df = df.loc[df[campo] == valor]
    return df


def transpone(df,rango,variable):
    indice = len(df.index)
    escenario = pd.DataFrame(index=df.index[rango:indice],columns=range(0,rango+1))
    #print(escenario)
    for i in range (0,indice-rango):
        temp = df.ix[df.index[i:i + rango+1], variable].values
        temp2 = np.transpose(temp)
        escenario.ix[escenario.index[i]] = temp2
    return escenario

def transpone2(df, rango, variable1,variable2):  #Build scenary with two variables
    indice = len(df.index)
    escenario = pd.DataFrame(index=df.index[rango:indice], columns=range(0, 2*rango))
    for i in range(0, indice - rango):
        temp = df.ix[df.index[i:i + rango], variable1].values
        temp1 = df.ix[df.index[i:i + rango], variable2].values
        temp2 = np.ravel(np.column_stack((temp,temp1)))
        temp3 = np.transpose(temp2)
        escenario.ix[escenario.index[i]] = temp3
    escenario.ix[escenario.index[0:indice - rango], 2 * rango] = df.ix[df.index[rango:indice], variable2]
    return escenario

def transpone3(df, rango, variable1, variable2,variable3):  #Build scenary with three variables
    indice = len(df.index)
    escenario = pd.DataFrame(index=df.index[rango:long], columns=range(0, 3 * rango))
    for i in range(0, indice - rango):
        temp = df.ix[df.index[i:i + rango], variable1].values
        temp2 = df.ix[df.index[i:i + rango], variable2].values
        temp3=df.ix[df.index[i:i + rango], variable3].values
        temp4 = np.ravel(np.column_stack((temp,temp2,temp3)))
        temp5 = np.transpose(temp4)
        escenario.ix[escenario.index[i]] = temp5
    escenario.ix[escenario.index[0:indice - rango], 3 * rango] = df.ix[df.index[rango:indice], variable3]
    return escenario


def renombracols(df,rango):
    cad = ''
    #print(df)
    for x in range(rango):
        cad = 'MES-' + str(rango-x)
        df.rename(index={0: 'Date'}, columns={x: cad}, inplace=True)

    cad = 'VAR'
    df.rename(index={0: 'Date'}, columns={rango : cad} , inplace=True)
    return df

def renombracols2(df,rango,var1,var2):
    for x in range(rango):
        a = x * 2
        b = a + 1
        cad = var1 + '-' + str(rango-x)
        cad2 = var2 + '-' + str(rango-x)
        df.rename(index={0: 'Date'}, columns={a: cad}, inplace=True)
        df.rename(index={0: 'Date'}, columns={b: cad2}, inplace=True)

    cad = 'VAR'
    df.rename(index={0: 'Date'}, columns={rango*2 : cad} , inplace=True)
    return df

def renombracols3(df,rango,var1,var2,var3):
    for x in range(rango):
        a = x * 3
        b = a + 1
        c = b + 1
        cad = var1 + '-' + str(rango-x)
        cad2 = var2 + '-' + str(rango-x)
        cad3 = var3 + '-' + str(rango-x)
        df.rename(index={0: 'Date'}, columns={a: cad}, inplace=True)
        df.rename(index={0: 'Date'}, columns={b: cad2}, inplace=True)
        df.rename(index={0: 'Date'}, columns={c: cad3}, inplace=True)

    cad = 'VAR'
    df.rename(index={0: 'Date'}, columns={rango*3 : cad} , inplace=True)
    return df


def fitradf(df, pr1, pr2):

    filtro = df.query('ANIO == ' + str(pr1) + ' && MES == ' + str(pr2))
    for a, b in filtro.iterrows():
        return b[0]
