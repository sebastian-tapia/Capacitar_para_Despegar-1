########## Ejercicio 1 ##########

pozo = 6000

def pozo_vacio(pozo):
    return pozo == 0


########## Ejercicio 2 ##########

def cuanta_gente_viaja_al_chalten(pozo):
    personas = pozo / 3000
    if personas >= 1:
        return int(personas)
    else:
        return 0


########## Ejercicio 3 ##########

def hasta_donde_llegamos(personas):
    dinero = pozo / personas 
    if dinero >= 3500:
        return "Tilcara"
    elif dinero >= 3000:
        return "Chaltén"
    elif dinero >= 2500:
        return "Mendoza"
    else:
        return "Segui Ahorrando"


########## Ejercicio 4 ##########

def aportar_al_pozo(aporte):
    global pozo
    pozo += aporte
    print(pozo)


########## Ejercicio 5 ##########

def darse_de_baja(se_bajan):
    devolucion = se_bajan * 500
    global pozo
    pozo -= devolucion


########## Ejercicio 6 ##########
ivg = 0
aplicacion_impuesto = 0

def calcular_monto_ivg(pozo):
    if pozo >= 15000:
        global ivg
        ivg = (pozo * 1.01) - pozo

def aplicar_ivg(ivg):
    global pozo
    global aplicacion_impuesto
    if ivg > 500:
        descuento = 500
        if aplicacion_impuesto < 3:
            aplicacion_impuesto += 1
            pozo -= descuento
            return pozo
    else:
        descuento = ivg
        pozo -= descuento
        return descuento



########## Ejercicio 7 ##########
# Modificar el ejericio 6 (hecho)


########## Ejercicio 8 ##########
dinero = pozo
def volver_a_empezar(dinero):
    global pozo
    if dinero < 1000:
        pozo = 0    


########## Ejercicio 9 ##########

delegado = ""

def declarar_delegado(candidato1, votos1, candidato2, votos2):
    global delegado
    if votos1 > votos2:
        delegado = candidato1 + " 2022"
    else:
        delegado = candidato2 + " 2022"


########## Ejercicio 9 ##########

delegados_por_anio = []

def registrar_delegado_del_anio(delegado,anio):
    global delegados_por_anio
    list.append(delegados_por_anio,delegado + " " + str(anio))

def registrar_delegado_del_anio_bis():
    global delegados_por_anio
    for x in range(3):
        delegado = input("Ingrese delegado:")
        #if delegado == 0:
            #return delegados_por_anio
        anio = str(input("Ingrese año:"))
        delegados_por_anio.append(delegado + " " + anio)



# raise (comando para generar un error)
# raise ValueError("string")