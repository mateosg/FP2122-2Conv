from reparaciones import *

def test_calcula_recaudacion(reparacion, centro, tipo=None):
    print(calcula_recaudacion(reparacion, centro, tipo))

def test_reparaciones_mas_largas(reparaciones, año, n, centro=None):
    print(reparaciones_mas_largas(reparaciones, año, n, centro))

def test_centro_mas_rapido(reparaciones, centros):
    print(centro_mas_rapido(reparaciones, centros))

def test_centros_experimentados_en(reparaciones, palabras_clave):
    print(centros_experimentados_en(reparaciones, palabras_clave))

def test_dias_entre_reparaciones(reparaciones):
    print(dias_entre_reparaciones(reparaciones))

####################### Llamadas a funciones de test #######################
if __name__=="__main__":
    reparaciones=lee_reparaciones("data/reparaciones.csv")
    '''
    Número total de reparaciones: 18
    Estos son los 3 primeros registros:
    '''
    print("Número total de reparaciones: {}".format(len(reparaciones)))
    print("Estos son los 3 primeros registros:")
    print(reparaciones[:3])

    ##################### Ejercicio 2 #####################
    print("\nRecaudación total en Sevilla de portátiles: ")
    test_calcula_recaudacion(reparaciones, "Sevilla", "portátil")
    print("Recaudación total en Sevilla de todo tipo de dispositivos: ")
    test_calcula_recaudacion(reparaciones, "Sevilla")
    ##################### Ejercicio 3 #####################
    print("\nLa reparación más larga de 2019 en Sevilla: ")
    test_reparaciones_mas_largas(reparaciones, 2019, 1, "Sevilla")
    print("Las 3 reparaciones más largas en 2020: ")
    test_reparaciones_mas_largas(reparaciones, 2020, 3)
    ##################### Ejercicio 4 #####################
    print("\nCentro más rápido: ")
    test_centro_mas_rapido(reparaciones, {"Sevilla", "Huelva", "Cádiz"})
    ##################### Ejercicio 5 #####################
    print("\nCentros experimentados en pantallas y baterías: ")
    test_centros_experimentados_en(reparaciones, {"pantalla", "batería"})
    ##################### Ejercicio 6 #####################
    print("\nDías entre reparaciones: ")
    test_dias_entre_reparaciones(reparaciones)
