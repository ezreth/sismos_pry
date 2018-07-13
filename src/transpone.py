import pandas as pd
import  numpy as np

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
    escenario = pd.DataFrame(index=df.index[rango:indice], columns=range(0, 3 * rango))
    for i in range(0, indice - rango):
        temp = df.ix[df.index[i:i + rango], variable1].values
        temp2 = df.ix[df.index[i:i + rango], variable2].values
        temp3=df.ix[df.index[i:i + rango], variable3].values
        temp4 = np.ravel(np.column_stack((temp,temp2,temp3)))
        temp5 = np.transpose(temp4)
        escenario.ix[escenario.index[i]] = temp5
    escenario.ix[escenario.index[0:indice - rango], 3 * rango] = df.ix[df.index[rango:indice], variable3]
    return escenario