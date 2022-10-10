########## Ejercicio 1 ##########

def obtener_indice(valor,lista):
    if valor in lista:
        posicion = list.index(lista,valor)
        return posicion
    else:
        return -1

    # contador = 0
    # if valor in lista:
    #     for i in lista:
    #         contador += 1
    #         if i == valor:
    #             return contador - 1
    # else:
    #     return -1




########## Ejercicio 2 ##########

def repetir(valor, cantidad):
    lista = []
    for i in range(0,cantidad):
        list.append(lista,valor)
    return lista

# def repetir(valor, cantidad):
#     return [i for i in range(0,cantidad)]




########## Ejercicio 3 ##########

def sumar_impares_hasta(numero):
    suma = 0
    for i in range(1,numero + 1 ,2):
        suma += i
    return suma




########## Ejercicio 4.1 ##########

def cuenta_regresiva(numero_inicial):
    lista = []
    for i in range(numero_inicial,-1,-1):
        list.append(lista,i)
    return lista

# def cuenta_regresiva(numero_inicial):
#     return [i for i in range(numero_inicial,-1,-1)]



########## Ejercicio 4.2 ##########

def invertir(lista):
    contador = 0
    lista2 = []
    for i in lista:
        contador -= 1
        list.append(lista2,lista[contador])
    return lista2

    # for i in lista:
    #     list.append(lista2,lista[-1])
    # return lista2
    # for dato in range(lista[-1],lista[0],-1):
    #     list.append(lista2,dato)
    # return lista2




########## Ejercicio 4.3 ##########

def remover_duplicados(lista):
    lista_sin_duplicados = []
    for i in lista:
        if i not in lista_sin_duplicados:
            list.append(lista_sin_duplicados,i)
    return lista_sin_duplicados

# def remover_duplicados(lista):
#     lista_sin_duplicados = []
#     lista_sin_duplicados = [i for i in lista if i not in lista_sin_duplicados]
#     return lista_sin_duplicados



########## Ejercicio 5 ##########

def repetir_letras(palabra,cantidad):
    repetir = ""
    for i in palabra:
        repetir = repetir + i * cantidad
    return repetir


# Falta convertir a string, no creo necesaria la lista de comprension
# def repetir_letras(palabra,cantidad):
#     repetir = ""
#     return str([repetir + i * cantidad for i in palabra])


########## Ejercicio 6 ##########

def capitalizar_palabras(string):
    if " " in string:
        string = string.title()
        return string
    else:
        return string    




########## Ejercicio 7 ##########

def sumar_seccion(lista,comienzo,cantidad):
    total = 0
    for i in lista[comienzo:comienzo + cantidad]:
        total += i
    return total




########## Ejercicio 8 ##########

def es_subconjunto(subconjunto, conjunto):
    esta = False
    for i in subconjunto:
        if i in conjunto:
            x = not esta
        else:
            x = esta
    return x

"""es_subconjunto([1, 2, 3], [1, 2]) esto da False como en el ejemplo
    pero si invierto el orden del primer parametro a es_subconjunto([3, 2, 1], [1, 2]) da True"""




########## Ejercicio 9 ##########

def tiene_bloque(lista):
    count = 0
    repetido = 0
    anterior = 0
    estado = False
    estado2 = True
    for i in lista:
        count += 1   
        anterior = lista[count - 1]
        if repetido != 3:
            if i == anterior:
                repetido += 1
        else:
            return not estado
    return repetido



########## Ejercicio 10 ##########

def es_palindromo(palabra):
    #palabra_invertida = invertir(palabra)
    palabra_a_string = ""
    for i in invertir(palabra):
        palabra_a_string += i
    return palabra == palabra_a_string




########## Ejercicio 11 ##########
unos_numeros = [3, 5, 9]
unos_string = ["mundo", "!"]

# def agregar_al_principio(lista, elemento):
#     lista_nueva = []
#     lista_nueva.append(elemento)
#     for i in lista:
#         lista_nueva.append(i)
#     print(lista_nueva)
#     print(unos_numeros)

# def agregar_al_principio(lista, elemento):
#     lista.insert(0,elemento)
#     print(lista)
#     print(unos_numeros)
# ya deja modificala la lista de manera global?