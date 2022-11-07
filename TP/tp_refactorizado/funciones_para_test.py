from tp_refactorizado import *
################ Funciones auxiliares ################

def realizar_compra_a_cinco_productos():
    localfisico.realizar_compra(100,25)
    localfisico.realizar_compra(99,50)
    localfisico.realizar_compra(1098,100)
    localfisico.realizar_compra(555,150)
    localfisico.realizar_compra(444,200)

def recargar_stock_a_cinco_productos():
    localfisico.recargar_stock(remera_m,200)
    localfisico.recargar_stock(remera_s,200)
    localfisico.recargar_stock(pulsera,200)
    localfisico.recargar_stock(campera_l,200)
    localfisico.recargar_stock(pantalon_m,200)

def registrar_cinco_productos():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(campera_l)
    localfisico.registrar_producto(pantalon_m)

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

def compra_virtual_de_200_ventas():
    localvirtual.registrar_producto(campera_l)
    localvirtual.registrar_producto(pantalon_m)
    localvirtual.registrar_producto(buzo_m)
    remera_s.agregar_categoria("remera de futbol")
    remera_m.agregar_categoria("remera de basquet")
    localvirtual.recargar_stock(555,500)
    localvirtual.recargar_stock(444,1000)
    localvirtual.recargar_stock(333,2000)
    for i in range(100):
        localvirtual.realizar_compra(555,1) # 4500 * 100 = 450000 
    for i in range(50):
        localvirtual.realizar_compra(444,1) # 50 * 50 = 2500        Total  677500
    for i in range(50):
        localvirtual.realizar_compra(333,1) # 4500 * 50 = 225000
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localvirtual.ventas_del_dia()

def compra_fisica_de_200_unidades():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(remera_s)
    localfisico.recargar_stock(100,500)
    localfisico.recargar_stock(1098,1000)
    localfisico.recargar_stock(99,2000)
    for i in range(100):
        localfisico.realizar_compra(100,1) # 4500 * 100 = 450000 
    for i in range(50):
        localfisico.realizar_compra(1098,1) # 50 * 50 = 2500        Total  677500
    for i in range(50):
        localfisico.realizar_compra(99,1) # 4500 * 50 = 225000
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localfisico.ventas_del_dia()


def compra_fisica_200():
    localfisico.registrar_producto(campera_l)
    localfisico.registrar_producto(pantalon_m)
    localfisico.registrar_producto(buzo_m)
    localfisico.recargar_stock(555,500)
    localfisico.recargar_stock(444,1000)
    localfisico.recargar_stock(333,2000)
    for i in range(100):
        localfisico.realizar_compra(555,1) # 4500 * 100 = 450000 
    for i in range(50):
        localfisico.realizar_compra(444,1) # 50 * 50 = 2500        Total  677500
    for i in range(50):
        localfisico.realizar_compra(333,1) # 4500 * 50 = 225000
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localfisico.ventas_del_dia()

    #haciendo Merge