

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