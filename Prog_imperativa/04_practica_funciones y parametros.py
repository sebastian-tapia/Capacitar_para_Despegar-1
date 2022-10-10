def sumar(a, b):
    return a + b

def dividir(a, b):
    return a / b

def restar(a, b):
    return a - b

def multiplicar(a,b):
    return a * b    

def es_par(numero):
    return numero % 2 == 0

def es_impar(numero):
    return not es_par(numero)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def nombre_completo(nombre, apellido):
    return nombre + apellido

def saludar(nombre):
    return "Hola " + nombre + ", un gusto conocerte"

def saludar_completo(nombre, apellido):
    return "Hola " + nombre + apellido + ", un gusto conocerte"

def obtener_datos_ciudad(nombre, poblacion, pais):
    return "La ciudad de " + nombre + " tiene una población de " + str(poblacion) + " habitantes y está ubicada en Argentina"

def convertir_horas_en_segundos(horas):
    return horas * 60 * 60

def calcular_perimetro_rectangulo(ancho, alto):
    return ancho * 2 + alto * 2

def calcular_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100

def sumar_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100 + numero

def restar_porcentaje(numero, porcentaje):
    return numero - (numero * porcentaje) / 100

def calcular_fps(fps, minutos):
    return (fps * 60) * minutos    

def obtener_rivales(a, b):
    return a + " vs " + b

def generar_email(usuario, dominio):
    return usuario + "@" + dominio + ".com"

def hace_calor(temperatura):
    return temperatura >= 22

def hace_frio(temperatura):
    return temperatura <= 12

def calcular_puntaje(facil, normal, dificil):
    return facil * 3 + normal * 5 + dificil * 10

def acepta_deposito(monto):
    return monto%10 == 0    