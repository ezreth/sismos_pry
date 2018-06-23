from read_csv import *
from splitdata import *

def crea_escenarios(lista):

    print('-Crea escenario ' + lista[3] + '-')

    df = read_csv('Segurodt')



    df = df.drop(lista[1], axis=1)

    set_group = df.groupby(lista[0])[lista[2]].apply(lambda x: x.astype(int).sum())


    training, test = get_train_test_inds(set_group)

    crea_csv(training,'etraining' + lista[3])
    crea_csv(test, 'etest' + lista[3])





