from read_csv import *
from splitdata import *

def crea_escenarios(lista):

    print('-Crea escenario' + lista[3] + '-')

    df = read_csv('../Data/Segurodt.csv')



    df = df.drop(lista[1], axis=1)

    set_group = df.groupby(lista[0])[lista[2]].apply(lambda x: x.astype(int).sum())


    training, test = get_train_test_inds(set_group,train_proportion=0.7)

    orden = lista[3]


    crea_csv(training,'etraining' + orden)
    crea_csv(test, 'etest1' + orden)





