from tp_macowins import *
import pytest


#####################  Tests de ejercicio 1  #####################

def test_registrar_un_producto():
    reiniciar_listas()
    #registrar_producto(remera_talle_m)
    registrar_producto({"codigo": 100, "nombre": "remera talle m", "categoria": "remera", "precio": 4500})
    assert len(codigos) == 1
    assert len(productos) == 1
    assert productos[0]["stock"] == 0

def test_registrar_dos_productos():
    reiniciar_listas()
    registrar_producto(remera_talle_s)
    registrar_producto(remera_talle_m)
    assert len(codigos) == 2
    assert len(productos) == 2

def test_no_registrar_productos_existentes():
    reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        registrar_producto(remera_talle_s)
        registrar_producto(remera_talle_m)
        registrar_producto(remera_talle_s)
    assert str(auxiliar.value) == "Producto ya registrado"
    assert len(productos) == 2
    

#####################  Tests de ejercicio 2  #####################

def test_recarga_de_stock_codigo_no_existe():
    reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        recargar_stock(100, 200)
    assert str(auxiliar.value) == "Codigo de producto ingresado no existe"
    

def test_recarga_de_stocks_a_dos_productos():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    recargar_stock(100, 200)
    recargar_stock(99, 50)
    assert productos[0]["stock"] == 200
    assert productos[1]["stock"] == 50
    recargar_stock(99, 50)
    assert productos[1]["stock"] == 100

#####################  Tests de ejercicio 3  #####################
# agregar test cn productos registrados y codigos inexistentes
def test_hay_stock_de_un_codigo_inexistente():
    reiniciar_listas()
    assert not hay_stock(99)


def test_hay_stock_de_un_codigo_existente_con_stock():
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    recargar_stock(100, 200)
    assert hay_stock(100)

def test_de_un_codigo_existente_sin_stock():
    assert not hay_stock(99)


#####################  Tests de ejercicio 4  #####################

def test_calcular_precio_final_si_es_extranejero_y_precio_mayor_a_70_precio_original_4500():
    assert calcular_precio_final(remera_talle_m,True) == 4500
    
def test_calcular_precio_si_no_es_extranjero_y_precio_es_menor_a_70_precio_original_50():
    assert calcular_precio_final(pulserita,False) == 60.5


#####################  Tests de ejercicio 5  #####################

def test_contar_una_categorias():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    assert contar_categorias(productos) == 1

def test_contar_dos_categorias():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    assert contar_categorias(productos) == 2


#####################  Tests de ejercicio 6  #####################

def test_realizar_dos_compras_de_codigo_existente_con_stock_y_descuento_de_su_stock():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    realizar_compra(100, 100)
    realizar_compra(99,50)
    assert len(ventas) == 2
    assert hay_stock(100)
    assert not hay_stock(99)


def test_realizar_una_compra_de_codigo_existente_con_stock_insuficiente():    
    with pytest.raises(ValueError) as auxiliar:
        realizar_compra(100, 150)
    assert str(auxiliar.value) == "No hay stock suficiente para la venta"
    assert len(ventas) == 2


def test_realizar_una_compra_de_codigo_inexistente():    
    assert realizar_compra(99999, 10) == "Código incorrecto o cantidad de items no puede ser menor a 1"

def test_realizar_una_compra_de_0_items_a_codigo_existente():    
    assert realizar_compra(100, 0) == "Código incorrecto o cantidad de items no puede ser menor a 1"


#####################  Tests de ejercicio 7  #####################
#test productos con stock no deberia eliminar ninguno

def test_eliminar_el_producto_sin_stock_de_tres_productos():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    discontinuar_productos(productos)
    assert len(productos) == 2

def test_eliminar_productos_sin_stock_de_tres_productos():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    discontinuar_productos(productos)
    assert len(productos) == 0

def test_hay_tres_productos_con_stock_no_deberia_eliminar_ninguno():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    recargar_stock(1098,100)
    assert len(productos) == 3


#####################  Tests de ejercicio 8  #####################

def test_ventas_del_dia_de_100_unidades_de_un_producto_y_carga_en_ventas():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    realizar_compra(100,100)
    assert valor_ventas_del_dia() == 450000


#se suman las ventas de 100 unidades anteriores más estas 50
def test_ventas_del_dia_de_50_unidades_de_un_producto_y_carga_en_ventas():
    ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    realizar_compra(99,50)
    assert valor_ventas_del_dia() == 675000
    assert len(ventas) == 4


#####################  Tests de ejercicio 9  #####################

#mantiene las compras del test anterior para no repetir codigo 
def test_ventas_del_anio_dos_productos():
    assert len(ventas_del_anio()) == 2 


#####################  Tests de ejercicio 10  #####################

def test_tres_productos_mas_vendidos():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    registrar_producto(campera_talle_l)
    registrar_producto(pantalon_talle_m)

    recargar_stock(100,200)
    recargar_stock(99,200)
    recargar_stock(1098,200)
    recargar_stock(555,200)
    recargar_stock(444,200)

    realizar_compra(100,25)
    realizar_compra(99,50)
    realizar_compra(1098,100)
    realizar_compra(555,150)
    realizar_compra(444,200)
    assert len(ventas) == 5
    assert contar_categorias(productos) == "Hay 4 categorias"
    assert productos_mas_vendidos(3)  == ["pantalon talle m", "campera talle l", "pulserita de tela verde"]


#####################  Tests de ejercicio 11  #####################
#se usa la lista productos generada en el test anterior
#test de mayusculas,espacios
#hacer que busque desde categoria no de posicion

def test_actualizar_precio_a_categoria_remera():
    actualizar_precios_por_categoria("remera",50)
    assert productos[0]["precio"] == 6750
    assert productos[1]["precio"] == 6750


def test_actualizar_precio_a_categoria_pulserita():
    actualizar_precios_por_categoria("accesorios",50)
    assert productos[2]["precio"] == 75

###