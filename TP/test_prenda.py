import pytest
from funciones_para_test import *
from prenda import *
from local import *

###############ejercicio 2##################


def test_recarga_stock_20_a_un_producto_devuelve_20():
    remera_m.recarga_stock(20)
    assert remera_m.stock_() == 20


def test_cargar_stock_a_un_producto_preguntar_si_tiene_stock_devuelve_True_():
    remera_m.restaurar_stock()

    remera_m.recarga_stock(20)
    assert remera_m.hay_stock()


def test_realizar_una_compra_de_un_producto_decrementa_su_stock_de_100_a_80():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_s)
    localfisico.recargar_stock(99,100)
    localfisico.realizar_compra(99,20)
    assert remera_s.stock_() == 80


####################### EJERCICIO 4 #######################

def test_precio_final_remera_m_y_sea_turista_es_4500():
    assert remera_m.calcular_precio_final(True)==4500

def test_precio_final_pulserita_y_no_sea_turista_es_60_5():
    assert pulsera.calcular_precio_final(False)==60.5


####################### Estados #######################

def test_de_prenda_con_estado_nuevo_devuelve_su_valor():
    remera_m.cambiar_estado(Nueva())
    assert remera_m.precio ==  4500 

def test_de_prenda_con_estado_promocion_de_500_pasa_a_valer_4000():
    remera_s.cambiar_estado(Promocion(500))
    assert remera_s.precio == 4000

def test_de_liquidacion_cambia_el_precio_del_producto_a_la_mitad_se_espera_25():
    pulsera.cambiar_estado(Liquidacion())
    assert pulsera.precio == 25

def test_pulsera_en_liquidacion_precio_cambia_a_12_5():
    pulsera.cambiar_estado(Liquidacion())
    assert pulsera.precio == 12.5

def test_pulsera_se_cambia_a_nueva_mantiene_su_precio_de_12_5():
    pulsera.cambiar_estado(Nueva())
    assert pulsera.precio == 12.5


####################### Categorias #######################

def test_producto_devuelve_si_es_de_categoria_remera():
    assert remera_m.categorias == ["remera"]

def test_se_agrega_categoria_a_remera_debe_devolver_dos_categorias():
    remera_m.agregar_categoria("remera de futbol")
    assert len(remera_m.categorias) == 2