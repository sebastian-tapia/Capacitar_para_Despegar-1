from local import *



################ Funciones auxiliares ################

def registrar_cinco_productos():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(campera_l)
    localfisico.registrar_producto(pantalon_m)

def registrar_cinco_productos_v2():
    localfisico.registrar_producto(remera_m_v2)
    localfisico.registrar_producto(remera_s_v2)
    localfisico.registrar_producto(pulsera_v2)
    localfisico.registrar_producto(campera_l_v2)
    localfisico.registrar_producto(pantalon_m_v2)

def registrar_cinco_productos_v3():
    localfisico.registrar_producto(remera_m_v3)
    localfisico.registrar_producto(remera_s_v3)
    localfisico.registrar_producto(pulsera_v3)
    localfisico.registrar_producto(campera_l_v3)
    localfisico.registrar_producto(pantalon_m_v3)


def recargar_stock_a_cinco_productos():
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,200)
    localfisico.recargar_stock(1098,200)
    localfisico.recargar_stock(555,200)
    localfisico.recargar_stock(444,200)

def recargar_stock_a_tres_productos():
    localfisico.recargar_stock(100,100)
    localfisico.recargar_stock(99,100)
    localfisico.recargar_stock(1098,100)


def realizar_compra_a_cinco_productos():
    localfisico.realizar_compra(100,25)
    localfisico.realizar_compra(99,50)
    localfisico.realizar_compra(1098,100)
    localfisico.realizar_compra(555,150)
    localfisico.realizar_compra(444,200)

def compra_fisico():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(remera_s)
    remera_s.agregar_categoria("remera de futbol")
    remera_m.agregar_categoria("remera de basquet")
    localfisico.recargar_stock(remera_m,500)
    localfisico.recargar_stock(pulsera,1000)
    localfisico.recargar_stock(remera_s,2000)
    localfisico.realizar_compra(99,4)
    localfisico.realizar_compra(1098,5)
    localfisico.realizar_compra(100,10)
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})

def compra_virtual():
    localvirtual.registrar_producto(remera_m)
    localvirtual.registrar_producto(pulsera)
    localvirtual.registrar_producto(remera_s)
    remera_s.agregar_categoria("remera de futbol")
    remera_m.agregar_categoria("remera de basquet")
    localvirtual.recargar_stock(100,500)
    localvirtual.recargar_stock(1098,1000)
    localvirtual.recargar_stock(99,2000)
    localvirtual.realizar_compra(99,4)
    localvirtual.realizar_compra(1098,5)
    localvirtual.realizar_compra(100,10)
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})


def compra_virtual_de_50_unidades():
    localvirtual.reiniciar_listas()
    localvirtual.registrar_producto(campera_l_v4)
    localvirtual.registrar_producto(pantalon_m_v4)
    localvirtual.registrar_producto(buzo_m_v4)
    campera_l_v4.agregar_categoria("campera camuflada")
    pantalon_m_v4.agregar_categoria("patalon camuflado")
    localvirtual.recargar_stock(555,500)
    localvirtual.recargar_stock(444,1000)
    localvirtual.recargar_stock(333,2000)
    for i in range(25):
        localvirtual.realizar_compra(555,1) # 35000 * 25 = 875000
    for i in range(10):
        localvirtual.realizar_compra(444,1) # 6000 * 10 = 60000         1017500
    for i in range(15):
        localvirtual.realizar_compra(333,1)  # 5500 * 15 = 82500
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localvirtual.ventas_del_dia()


def compra_virtual_de_200_ventas():
    localvirtual.reiniciar_listas()
    localvirtual.registrar_producto(campera_l_v4)
    localvirtual.registrar_producto(pantalon_m_v4)
    localvirtual.registrar_producto(buzo_m_v4)
    campera_l_v4.agregar_categoria("campera camuflada")
    pantalon_m_v4.agregar_categoria("patalon camuflado")
    localvirtual.recargar_stock(555,500)
    localvirtual.recargar_stock(444,1000)
    localvirtual.recargar_stock(333,2000)
    for i in range(100):
        localvirtual.realizar_compra(555,1) 
    for i in range(50):
        localvirtual.realizar_compra(444,1) 
    for i in range(50):
        localvirtual.realizar_compra(333,1) 
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localvirtual.ventas_del_dia()

def compra_fisica_de_200_unidades():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m_v3)
    localfisico.registrar_producto(pulsera_v3)
    localfisico.registrar_producto(remera_s_v3)
    localfisico.recargar_stock(100,500)
    localfisico.recargar_stock(1098,1000)
    localfisico.recargar_stock(99,2000)
    for i in range(100):
        localfisico.realizar_compra(100,1)  # 35000 * 100 = 3500000
    for i in range(50):
        localfisico.realizar_compra(1098,1) # 6000 * 50 = 300000       Total  4075000
    for i in range(50):
        localfisico.realizar_compra(99,1)   # 5500 * 50 = 275000
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localfisico.ventas_del_dia()


def compra_fisica_200():
    localfisico.registrar_producto(campera_l_v5)
    localfisico.registrar_producto(pantalon_m_v5)
    localfisico.registrar_producto(buzo_m_v5)
    localfisico.recargar_stock(555,500)
    localfisico.recargar_stock(444,1000)
    localfisico.recargar_stock(333,2000)
    for i in range(100):
        localfisico.realizar_compra(555,1) # 35000 * 100 = 3500000
    for i in range(50):
        localfisico.realizar_compra(444,1) # 6000 * 50 = 300000       Total  4075000
    for i in range(50):
        localfisico.realizar_compra(333,1) # 5500 * 50 = 275000
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localfisico.ventas_del_dia()


remera_m_v2 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v2 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v2 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v2 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v2 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v2 = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v3 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v3 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v3 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v3 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v3 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v3 = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v4 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v4 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v4 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v4 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v4 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v4 = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v5 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v5 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v5 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v5 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v5 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v5 = Prenda(333,"buzo talle m", "buzo", 5500)


    