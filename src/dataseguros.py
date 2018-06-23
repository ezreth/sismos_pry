from escenarios import *

def main():

    print("-GENERACION DE ESCENARIOS-")
    print("MODELADO DE DATOS")
    print("PROYECTO: INFORMACION DE SEGUROS")
    print("INTEGRANTES:")
    print("NATALIA CARVAJAL")
    print("KARINA MOLINA")
    print("DIEGO LÓPEZ")

    e1 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'IMPUESTO', 'TAMANIO', 'UTILIDADES'], ["INGRESOS"], "1"]
    #crea_escenarios(e1)

    e2 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'IMPUESTO', 'TAMANIO', 'INGRESOS'], ["UTILIDADES"], "2"]
    crea_escenarios(e2)

    e3 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'UTILIDADES', 'TAMANIO', 'INGRESOS'], ["IMPUESTO"], "3"]
    crea_escenarios(e3)

    e4 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'IMPUESTO', 'TAMANIO'], ["INGRESOS","UTILIDADES"], "4"]
    crea_escenarios(e4)

    e5 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'UTILIDADES', 'TAMANIO'], ["INGRESOS","IMPUESTO"], "5"]
    crea_escenarios(e5)

    e6 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'TAMANIO', 'INGRESOS'], ["UTILIDADES","IMPUESTO"], "6"]
    crea_escenarios(e6)

    e7 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA'], ['COD', 'TAMANIO'], ["INGRESOS","UTILIDADES", "IMPUESTO"], "7"]
    crea_escenarios(e7)

    e8 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA','TAMANIO'], ['COD', 'IMPUESTO', 'UTILIDADES'], ["INGRESOS"], "8"]
    crea_escenarios(e8)

    e9 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'TAMANIO'], ['COD', 'IMPUESTO', 'INGRESOS'], ["UTILIDADES"], "9"]
    crea_escenarios(e9)

    e10 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'TAMANIO'], ['COD', 'UTILIDADES', 'INGRESOS'], ["IMPUESTO"], "10"]
    crea_escenarios(e10)

    e11 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'TAMANIO'], ['COD', 'IMPUESTO'], ["INGRESOS", "UTILIDADES"], "11"]
    crea_escenarios(e11)

    e12 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'TAMANIO'], ['COD', 'UTILIDADES'], ["INGRESOS", "IMPUESTO"], "12"]
    crea_escenarios(e12)

    e13 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'TAMANIO'], ['COD', 'INGRESOS'], ["UTILIDADES", "IMPUESTO"], "13"]
    crea_escenarios(e13)

    e14 = [['ANIO', 'REGION', 'SECTOR', 'PROVINCIA', 'TAMANIO'], ['COD'], ["INGRESOS","UTILIDADES", "IMPUESTO"], "14"]
    crea_escenarios(e14)

    print("-FIN-")




if __name__ == "__main__":
    main()


