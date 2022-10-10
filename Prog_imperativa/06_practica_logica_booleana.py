# Ejercicio 1

def puede_ver_pelicula(edad, tiene_autorizacion):
    return edad >= 15 or tiene_autorizacion


# Ejercicio 2

def esta_en_rango(valor, minimo, maximo):
    return valor >= minimo and valor <= maximo


# Ejercicio 3

def puede_avanzar(color_semaforo):
    return color_semaforo == "verde"


#Eercicio 4

def es_vocal(letra):
    return letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"


# Ejercicio 5

def es_consonante(letra):
    return not es_vocal(letra)


# Ejercicio 6

def es_hora_valida(hora):
    separa = hora.split(":")
    return int(separa[0]) < 23 and int(separa[1]) < 59
print(es_hora_valida("00:00"))


# Ejercicio 7

def puede_renovar_carnet(paso_test, tiene_multas_impagas, pago_impuestos):
    return paso_test and not tiene_multas_impagas and pago_impuestos

"""print(puede_renovar_carnet(True, True, True))    # False
print(puede_renovar_carnet(True, True, False))   # False
print(puede_renovar_carnet(True, False, True))   # True
print(puede_renovar_carnet(True, False, False))  # False
print(puede_renovar_carnet(False, True, True))   # False
print(puede_renovar_carnet(False, True, False))  # False
print(puede_renovar_carnet(False, False, True))  # False
print(puede_renovar_carnet(False, False, False)) # False"""


# Ejercicio 8

def puede_graduarse(asistencia, materias_aprobadas, tesisAprobada):
    return asistencia >= 75 and materias_aprobadas >= 50 and tesisAprobada

"""print(puede_graduarse(80, 50, True))  # True
print(puede_graduarse(80, 50, False)) # False
print(puede_graduarse(80, 45, True))  # False
print(puede_graduarse(80, 45, False)) # False
print(puede_graduarse(65, 50, True))  # False
print(puede_graduarse(33, 55, False)) # False
print(puede_graduarse(42, 45, True))  # False
print(puede_graduarse(28, 45, False)) # False"""


# Ejercicio 9

def comienza_con_a(string):
    return string.startswith("a") or string.startswith("A")


# Ejercicio 10

def es_multiplo_de_3(numero):
    return numero % 3 == 0


# Ejercicio 11

def es_bisiesto(año):
    return año % 400 == 0 or (año % 4 == 0 and not año % 100 == 0)


# Ejercicio de la clase 12-09-2022

def a_quien_le_toca(dia):
    if dia == "lunes":
        return "Ana y Dani"
    elif dia == "jueves":
        return "Fran y Ana"
    else:
        return "no hay clases"    


# https://flbulgarelli.github.io/recursos-python/  introduccion... el 6 y 8