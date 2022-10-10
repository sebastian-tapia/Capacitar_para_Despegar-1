############### Ejercicio 1 ###############

def inversa(numero):
    if numero == 0:
        return 0
    else:
        return 1 / numero
#print(inversa(0))


############### Ejercicio 2 ###############

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
#print(par_o_impar(10))


############### Ejercicio 3 ###############

def positivo_o_negativo(numero):
    if numero > 0:
        return "positivo"
    else:
        return "negativo"


############### Ejercicio 4 ###############

def avanzar_semaforo(color_actual):
    if color_actual == "verde":
        return "amarillo"
    elif color_actual == "amarillo":
        return "rojo"
    elif color_actual == "rojo":
        return "verde"
    else:
        return "ingrese color correcto"
#print(avanzar_semaforo("azul"))


############### Ejercicio 5 ###############

def obtener_dias_mes(mes):
    if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
        return 31
    elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
        return 30
    elif mes == "febrero":
        return 28
    else:
        return "Ingrese mes correcto"
#print(obtener_dias_mes(""))


############### Ejercicio 6 ###############

def obtener_generacion(anio_nacimiento):
    if anio_nacimiento >= 1949 and anio_nacimiento <= 1968:
        return "Baby boomer"
    elif anio_nacimiento >= 1969 and anio_nacimiento <= 1980:
        return "Generación X"
    elif anio_nacimiento >= 1981 and anio_nacimiento <= 1993:
        return "Millennials"
    elif anio_nacimiento >= 1994 and anio_nacimiento <= 2010:
        return "Generación Z"
    else:
        return "?"
#print(obtener_generacion(1990))

############### Ejercicio 7 ###############

def obtener_sensacion(temperatura):
    if temperatura >= 30:
        return "¡Hace mucho calor!"
    elif temperatura >= 25 and temperatura < 30:
        return "Hace calor"
    elif temperatura >= 15 and temperatura < 25:
        return "Está lindo"
    elif temperatura >= 0 and temperatura < 15:
        return "¡Hace frío!"
    else:
        return "¡Está helando!"
#print(obtener_sensacion())

############### Ejercicio 8 ###############

def obtener_nota(puntaje):
    if puntaje < 0 or puntaje > 10:
        return "Puntaje invalido"
    elif puntaje >= 6 and puntaje < 7:
        return "Regular"
    elif puntaje >= 7 and puntaje < 8:
        return "Bueno"
    elif puntaje >= 8 and puntaje < 10:
        return "Muy bueno"
    elif puntaje == 10:
        return "Excelente"
    else:
        return "Desaprobado"
#print(obtener_nota())


############### Ejercicio 9 ###############

def jugar_piedra_papel_tijera(a, b):
    if a == "piedra" and b == "tijera" or a == "tijera" and b == "piedra":
        return "¡Ganó Piedra!"
    elif a == "tijera" and b == "papel" or a == "papel" and b == "tijera":
        return "¡Ganó tijera!"
    elif a == "papel" and b == "piedra" or a == "piedra" and b == "papel":
        return "¡Ganó papel!"
    else:
        return "¡Empate!"

"""print(jugar_piedra_papel_tijera('tijera', 'piedra'))  # ¡Ganó piedra!
print(jugar_piedra_papel_tijera('piedra', 'tijera'))  # ¡Ganó piedra!
print(jugar_piedra_papel_tijera('papel', 'piedra'))   # ¡Ganó papel!
print(jugar_piedra_papel_tijera('piedra', 'papel'))   # ¡Ganó papel!
print(jugar_piedra_papel_tijera('papel', 'tijera'))   # ¡Ganó tijera!
print(jugar_piedra_papel_tijera('tijera', 'papel'))   # ¡Ganó tijera!
print(jugar_piedra_papel_tijera('piedra', 'piedra'))  # ¡Empate!
print(jugar_piedra_papel_tijera('papel', 'papel'))    # ¡Empate!
print(jugar_piedra_papel_tijera('tijera', 'tijera'))  # ¡Empate!"""


############### Ejercicio 10 ###############

def celsius_a_farenheit(grados):
    return grados * 1.8 + 32
#print(celsius_a_farenheit())


############### Ejercicio 11 ###############

def farenheit_a_celsius(grados):
    return (grados - 32) / 1.8
#print(farenheit_a_celsius())


############### Ejercicio 12 ###############

def hace_frio_celsius(grados):
    return grados < 8

def hace_frio_farenheit(grados):
    return hace_frio_celsius(farenheit_a_celsius(grados))
#print(hace_frio_farenheit())


############### Ejercicio 13 ###############

def maximo_entre_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
#print(maximo_entre_tres(22,283,294))

def minimo_entre_tres(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
#print(minimo_entre_tres(22,283,294))

def dispersion(a, b, c):
    return maximo_entre_tres(a, b, c) - minimo_entre_tres(a, b, c)
#print(dispersion(22, 283, 294))


############### Ejercicio 14 ###############

def dias_parejos(a, b, c):
    return dispersion(a, b, c) < 30

def dias_locos(a, b, c):
    return dispersion(a, b, c) > 100

def dias_normales(a, b, c):
    return not dias_parejos(a, b, c) and not dias_locos(a, b, c)
#print(dias_normales(1, 200, 500))


############### Ejercicio 15 ###############

def peso_pino(metros):
    if metros > 3:
        return 3 * 300 + (metros - 3) * 200
    else:
        return 3 * 200

def es_peso_util(kg):
    return kg >= 400 and kg <= 1000

def sirve_pino(metros):
    return es_peso_util(peso_pino(metros))
#print(sirve_pino(3))    


############### Ejercicio 16 ###############

def punto_para_setenta(numero):
    if numero == 1:
        return 5.5
    elif numero == 10 or numero == 11 or numero == 12:
        return 0.5
    else:
        return numero