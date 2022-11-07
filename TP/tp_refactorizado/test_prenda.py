import pytest
from tp_refactorizado import *

###############ejercicio 2##################


def test_recarga_stock_20_a_un_producto_devuelve_20():
    remera_m.recargar_stock(20)
    assert remera_m.stock_() == 20


def test_cargar_stock_a_un_producto_preguntar_si_tiene_stock_devuelve_True_():
    remera_m.restaurar_stock()

    remera_m.recargar_stock(20)
    assert remera_m.hay_stock()

####################### EJERCICIO 4 #######################

def test_precio_final_remera_m_y_sea_turista_es_4500():
    assert remera_m.calcular_precio_final(True)==4500

def test_precio_final_pulserita_y_no_sea_turista_es_60_5():
    assert pulsera.calcular_precio_final(False)==60.5


 ################################################3

def test_realizar_una_compra_de_un_producto_decrementa_su_stock_de_100_a_80():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_s)
    localfisico.recargar_stock(remera_s,100)
    localfisico.realizar_compra(99,20)
    assert remera_s.stock_() == 80      

