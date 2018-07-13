from read_csv import *
from splitdata import *
from transpone import *
from renombracol import *

def crea_escenarios(lista, rango, filtro):

    print('-Crea escenarios-')

    df = read_csv('Segurosdb')

    df = df.drop(lista[1], axis=1)
    vars = len(lista[2])

    if filtro != '':
        df = df.loc[df['COD'] == filtro]

    set_group = df.groupby(lista[0])[lista[2]].apply(lambda x: x.astype(int).sum())

    set_group = set_group.groupby(lista[3])[lista[2]].apply(lambda y: y.astype(int).sum())

    set_group.sort_values(lista[3], ascending=[False, True], inplace=True)

    #print(set_group)

    if vars == 1:
        esc = transpone(set_group,rango,lista[2])
        df = renombracols(esc, rango)
        crea_csv(df, 'Esc' + filtro + str(lista[2][0]) + str(rango) + 'M')
    elif vars == 2:
        esc = transpone2(set_group,rango,lista[2][0],lista[2][1])
        df = renombracols2(esc, rango, lista[2][0], lista[2][1])
        crea_csv(df, 'Esc' + filtro + str(lista[2][0]) + str(lista[2][1]) + str(rango) + 'M')
    else:
        esc = transpone3(set_group,rango,lista[2][0],lista[2][1],lista[2][2])
        df = renombracols3(esc,rango,lista[2][0],lista[2][1],lista[2][2])
        crea_csv(df, 'Esc' + filtro + str(lista[2][0]) + str(lista[2][1]) + str(lista[2][2]) + str(rango) + 'M')


'''

def filtra_escenario(campo,valor,df):
    df = df.loc[df[campo] == valor]

    return df

def fitradf(df, pr1, pr2):

    filtro = df.query('ANIO == ' + str(pr1) + ' && MES == ' + str(pr2))
    for a, b in filtro.iterrows():
        return b[0]


'''

