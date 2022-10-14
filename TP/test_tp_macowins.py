from tp_macowins import *
import pytest


#####################  Tests de ejercicio 1  #####################

def test_registrar_un_producto():
    reiniciar_listas()
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

def test_recarga_de_stock_codigo_inexiste():
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

def test_no_hay_stock_de_un_codigo_no_cargado():
    reiniciar_listas()
    assert not hay_stock(99)

def test_hay_stock_de_un_codigo_existente_con_stock():
    reiniciar_listas()
    registrar_tres_productos_y_recargar_stock_a_dos()
    assert hay_stock(100)

def test_de_codigo_existente_sin_stock():
    reiniciar_listas()
    registrar_tres_productos_y_recargar_stock_a_dos()
    assert not hay_stock(99)

def test_de_codigo_inexistente_cuando_hay_productos_cargados():
    reiniciar_listas()
    registrar_tres_productos_y_recargar_stock_a_dos()
    assert not hay_stock(98767)

#####################  Tests de ejercicio 4  #####################

def test_calcular_precio_final_si_es_extranejero_y_precio_mayor_a_70_con_precio_original_4500():
    assert calcular_precio_final(remera_talle_m,True) == 4500
    
def test_calcular_precio_si_no_es_extranjero_y_precio_es_menor_a_70_con_precio_original_50():
    assert calcular_precio_final(pulserita,False) == 60.5


#####################  Tests de ejercicio 5  #####################

def test_registrar_dos_productos_de_la_misma_categoria_debe_devolver_una_categoria():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    assert contar_categorias(productos) == 1

def test_registrar_tres_productos_siendo_dos_de_la_misma_debe_devolver_dos_categorias():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    assert contar_categorias(productos) == 2


#####################  Tests de ejercicio 6  #####################

def test_realizar_dos_compras_de_codigo_existente_debe_agregar_dos_ventas():
    reiniciar_listas()
    registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()
    assert len(ventas) == 2


def test_realizar_dos_compras_de_codigo_existente_con_stock_debe_decrementar_stock_del_ultimo():
    reiniciar_listas()
    registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()
    #assert hay_stock(100)
    assert not hay_stock(99)


def test_realizar_una_compra_de_codigo_existente_con_stock_insuficiente_debe_entrar_en_excepcion():
    reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()
        realizar_compra(100, 150)
    assert str(auxiliar.value) == "No hay stock suficiente para la venta"


def test_realizar_una_compra_de_codigo_existente_con_stock_insuficiente_no_debe_aumentar_ventas():
    reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()
        realizar_compra(100, 150)
    assert len(ventas) == 2


def test_realizar_una_compra_de_codigo_inexistente():
    reiniciar_listas()
    registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()   
    assert realizar_compra(99999, 10) == "Código incorrecto o cantidad de items no puede ser menor a 1"


def test_realizar_una_compra_de_0_items_a_codigo_existente():
    reiniciar_listas()
    registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()    
    assert realizar_compra(100, 0) == "Código incorrecto o cantidad de items no puede ser menor a 1"


#####################  Tests de ejercicio 7  #####################

def test_eliminar_el_producto_sin_stock_de_tres_productos():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    discontinuar_productos(productos)
    assert len(productos) == 2

def test_eliminar_tres_productos_sin_stock_de_una_lista_de_tres_productos_sin_stock():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    discontinuar_productos(productos)
    assert len(productos) == 0

def test_lista_de_cinco_productos_con_stock_no_se_deberia_eliminar_ninguno():
    reiniciar_listas()
    registrar_cinco_productos()
    recargar_stock_a_cinco_productos()
    discontinuar_productos(productos)
    assert len(productos) == 5


#####################  Tests de ejercicio 8  #####################

def test_realizar_una_compra_del_dia_de_100_unidades_de_un_producto_que_cuesta_4500_debe_devolver_450000():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    realizar_compra(100,100)
    assert valor_ventas_del_dia() == 450000


#a la lista de ventas se le agrega dos productos comprados con otras fechas
def test_ventas_del_dia_de_150_unidades_entre_dos_productos_debe_devolver_total_precio_de_675000():
    reiniciar_listas()
    registrar_tres_productos_recargar_a_dos_y_comprar_a_dos()
    ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    assert valor_ventas_del_dia() == 675000
    


#####################  Tests de ejercicio 9  #####################

#a la lista de ventas se le agrega dos productos comprados con otras fechas
def test_cuatro_ventas_en_total_dos_de_este_año_debe_devolver_dos_ventas_del_anio():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    realizar_compra(100,100)
    realizar_compra(99,50)
    ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    assert len(ventas_del_anio()) == 2 


#####################  Tests de ejercicio 10  #####################

def test_debe_devolver_los_nombres_de_los_tres_productos_mas_vendidos_en_orden_descendente():
    reiniciar_listas()
    registrar_cinco_productos()
    recargar_stock_a_cinco_productos()
    realizar_compra_a_cinco_productos()
    assert productos_mas_vendidos(3)  == ["pantalon talle m", "campera talle l", "pulserita de tela verde"]

def test_debe_devolver_los_nombres_de_los_cuatro_productos_mas_vendidos_en_orden_descendente():
    reiniciar_listas()
    registrar_cinco_productos()
    recargar_stock_a_cinco_productos()
    realizar_compra_a_cinco_productos()
    assert productos_mas_vendidos(4)  == ["pantalon talle m", "campera talle l", "pulserita de tela verde", "remera talle s"]

#####################  Tests de ejercicio 11  #####################

def test_en_una_lista_de_cinco_productos_actualizar_precio_a_categoria_remera_mal_escrita_en_un_50_porciento_debe_actualizar_el_precio_a_6750():
    reiniciar_listas()
    registrar_cinco_productos()
    actualizar_precios_por_categoria(" reMera ",50)
    assert productos[0]["precio"] == 6750
    assert productos[1]["precio"] == 6750


def test_actualizar_precio_a_categoria_accesorios_mal_escrita_en_50_porciento_debe_actualizar_el_precio_a_75():
    reiniciar_listas()
    registrar_cinco_productos()
    actualizar_precios_por_categoria(" aCceSoriOs",50)
    assert productos[2]["precio"] == 75







#funciones auxiliares
def registrar_cinco_productos():
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    registrar_producto(campera_talle_l)
    registrar_producto(pantalon_talle_m)

def recargar_stock_a_cinco_productos():
    recargar_stock(100,200)
    recargar_stock(99,200)
    recargar_stock(1098,200)
    recargar_stock(555,200)
    recargar_stock(444,200)

def realizar_compra_a_cinco_productos():
    realizar_compra(100,25)
    realizar_compra(99,50)
    realizar_compra(1098,100)
    realizar_compra(555,150)
    realizar_compra(444,200)

def registrar_tres_productos_recargar_a_dos_y_comprar_a_dos():
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100,200)
    recargar_stock(99,50)
    realizar_compra(100, 100)
    realizar_compra(99,50)

def registrar_tres_productos_y_recargar_stock_a_dos():
    registrar_producto(remera_talle_m)
    registrar_producto(remera_talle_s)
    registrar_producto(pulserita)
    recargar_stock(100, 200)
    recargar_stock(1098, 200)