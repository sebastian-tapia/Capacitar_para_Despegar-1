from tp_macowins import *
import pytest


#####################  Tests de ejercicio 1  #####################

def test_registrar_un_producto():
    registrar_producto(remera_talle_m)
    assert len(codigos) == 1
    assert productos == [{
                            "codigo": 100,
                            "nombre": "remera talle m",
                            "categoria": "remera",
                            "precio": 4500,
                            "stock":0
                        }]

def test_registrar_dos_productos():
    registrar_producto(remera_talle_s)
    assert len(codigos) == 2
    assert len(productos) == 2
    


def test_no_registrar_productos_existente():
    with pytest.raises(ValueError):
        registrar_producto(remera_talle_s)
    assert "Producto ya registrado"
    assert len(codigos) == 2


#####################  Tests de ejercicio 2  #####################

def test_recarga_de_stock_codigo_no_existe():
    with pytest.raises(ValueError):
        recargar_stock(8887778, 200)
    assert "Codigo de producto ingresado no existe"
    

def test_recarga_de_stock_a_un_codigo_cuando_hay_dos_productos():
    recargar_stock(100, 200)
    assert productos[0]["stock"] == 200 



#####################  Tests de ejercicio 3  #####################

def test_hay_stock_de_un_codigo_inexistente():
    assert hay_stock(454545) == False

#en los assert puedo poner cualquier cosa y funciona
def test_hay_stock_de_un_codigo_existente_con_stock():
    assert hay_stock(100) == "Hay stock de 200 remera talle m"

def test_hay_stock_de_un_codigo_existente_sin_stock():
    assert hay_stock(99) == "No hay stock de remera talle s"


#####################  Tests de ejercicio 4  #####################

def test_calcular_precio_final_si_es_extranejero_y_precio_mayor_a_50():
    assert calcular_precio_final(remera_talle_m,True) == 4500
    
def test_calcular_precio_si_no_es_extranjero_y_precio_es_menor_a_50():
    assert calcular_precio_final(pulserita,False) == 60.5


#####################  Tests de ejercicio 5  #####################

def test_contar_categorias_hay_dos_categorias_iguales():
    assert contar_categorias(productos) == "Hay 1 categorias"


#####################  Tests de ejercicio 6  #####################

def test_realizar_una_compra_de_codigo_existente_con_stock():
    realizar_compra(100, 100)
    assert len(ventas) == 1
    assert hay_stock(100) == "Hay stock de 100 remera talle m"

# def test_realizar_una_compra_de_codigo_existente_sin_stock():    
#     with pytest.raises(ValueError(realizar_compra(99, 100))):
#         assert "No hay stock suficiente para la venta"


#####################  Tests de ejercicio 7  #####################

def test_eliminar_el_producto_sin_stock_de_dos_productos():
    discontinuar_productos(productos)
    assert len(productos) == 1


#####################  Tests de ejercicio 8  #####################

def test_ventas_de_100_unidades_de_un_producto():
    assert valor_ventas_del_dia() == "El valor total de ventas de hoy es de: $450000"


#####################  Tests de ejercicio 9  #####################

def test_ventas_del_anio_un_solo_producto():
    ventas_del_anio()
    assert len(ventas_del_anio_actual) == 1


#####################  Tests de ejercicio 10  #####################

def test_productos_mas_vendidos():
    assert productos_mas_vendidos(1)  == ["remera talle m"]


#####################  Tests de ejercicio 11  #####################

def test_actualizar_precio_a_categoria_remera():
    actualizar_precios_por_categoria("remera",50)
    assert productos[0]["precio"] == 6750