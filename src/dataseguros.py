from escenarios import *

def main():

    print("-GENERACION DE ESCENARIOS-")
    print("MODELADO DE DATOS")
    print("PROYECTO: INFORMACION DE SEGUROS")
    print("INTEGRANTES:")
    print("NATALIA CARVAJAL")
    print("KARINA MOLINA")
    print("DIEGO LÓPEZ")

    rango = 6
    filtro = 'F'

    #una variable
    e1 = [['ANIO', 'MES', 'COD', 'SECTOR'], ['UTILIDAD', 'TAMANIO', 'IMPUESTO', 'REGION', 'PROVINCIA'], ["INGRESO"], ['ANIO', 'MES']]
    crea_escenarios(e1, rango, filtro)

    e2 =  [['ANIO', 'MES', 'COD', 'SECTOR'], ['INGRESO', 'TAMANIO', 'IMPUESTO', 'REGION', 'PROVINCIA'], ["UTILIDAD"], ['ANIO', 'MES']]
    crea_escenarios(e2, rango, filtro)

    e3 = [['ANIO', 'MES', 'COD', 'SECTOR'], ['UTILIDAD', 'TAMANIO', 'INGRESO', 'REGION', 'PROVINCIA'], ["IMPUESTO"], ['ANIO', 'MES']]
    crea_escenarios(e3, rango, filtro)

    #dos variables
    e4 = [['ANIO', 'MES', 'COD', 'SECTOR'], ['IMPUESTO', 'TAMANIO', 'REGION','PROVINCIA'], ["INGRESO","UTILIDAD"], ['ANIO', 'MES']]
    crea_escenarios(e4, rango, filtro)

    e5 = [['ANIO', 'MES', 'COD', 'SECTOR'], ['UTILIDAD', 'TAMANIO', 'REGION','PROVINCIA'], ["INGRESO","IMPUESTO"], ['ANIO', 'MES']]
    crea_escenarios(e5, rango, filtro)

    e6 = [['ANIO', 'MES', 'COD', 'SECTOR'], ['INGRESO', 'TAMANIO', 'REGION','PROVINCIA'], ["UTILIDAD","IMPUESTO"], ['ANIO', 'MES']]
    crea_escenarios(e6, rango, filtro)

    #tres variables
    e14 = [['ANIO', 'MES', 'COD', 'SECTOR'], ['REGION','PROVINCIA','TAMANIO'], ["INGRESO", "IMPUESTO", "UTILIDAD"],['ANIO', 'MES']]
    crea_escenarios(e14, rango, filtro)

    print("-FIN-")




if __name__ == "__main__":
    main()


