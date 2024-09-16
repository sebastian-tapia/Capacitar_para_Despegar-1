import pytest
from funciones_para_test import *
from local import *

####################### Ejercicio 1 #######################

def test_se_registra_una_prenda_en_local_tiene_1_producto():
    local.registrar_producto(remera_m)
    assert len(local.productos)==1

def test_se_registra_tres_prendas_en_local_tiene_3_producto():
    local.reiniciar_listas()
    local.registrar_producto(pantalon_m)
    local.registrar_producto(remera_s)
    local.registrar_producto(remera_m)
    assert len(local.productos)==3

def test_se_agregra_productos_repetido_se_espera_el_RAISE_exception():
    localfisico = Fisico(3250)
    localfisico.reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        localfisico.registrar_producto(remera_s)
        localfisico.registrar_producto(remera_s)     
    assert str(auxiliar.value) == "Producto ya registrado"


####################### Ejercicio 3 #######################

def test_agrego_2_productos_distintas_categorias_deberia_devolver_2():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(pulsera)
    assert localfisico.contar_categorias() == 2

def test_registrar_2_productos_misma_categoria_devuelve_1():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    assert localfisico.contar_categorias() == 1

####################### Ejercio 4 #######################

def test_al_realizar_una_compra_se_agregar_el_producto_a_ventas_y_largo_de_ventas_es_1():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,100)
    localfisico.realizar_compra(100,20)
    assert len(localfisico.ventas) == 1

def test_al_realizar_dos_compras_se_agrega_el_producto_a_ventas_y_largo_de_ventas_es_2():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,100)
    localfisico.realizar_compra(100,20)
    localfisico.realizar_compra(100,10)
    assert len(localfisico.ventas)==2

####################### Ejercicio 5 #######################

def test_remueve_todos_los_productos_con_stock_en_0():
    localf=Fisico(3250)
    localf.reiniciar_listas()
    localf.registrar_producto(remera_s)
    localf.registrar_producto(pantalon_m)
    localf.discontinuar_productos()
    assert len(localf.productos) == 0

def test_elimina_el_producto_sin_stock_de_tres_productos_la_lista_productos_debe_ser_2():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(1098,50)
    localfisico.discontinuar_productos()
    assert len(localfisico.productos) == 2


def test_hay_tres_productos_con_stock_no_deberia_eliminar_ninguno_largo_de_Lista_debe_ser_3():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,50)
    localfisico.recargar_stock(1098,100)
    localfisico.discontinuar_productos()
    assert len(localfisico.productos) == 3

    ####################### EJERCICIO 6 #######################

def test_realizar_una_compra_del_dia_de_100_unidades_de_un_producto_que_cuesta_4500_debe_devolver_450000():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,50)
    localfisico.realizar_compra(100,100)
    assert localfisico.valor_ventas_del_dia() == 450000


def test_ventas_del_dia_de_150_unidades_entre_dos_productos_debe_devolver_675000():
    #a la lista de ventas se le agrega dos productos comprados con otras fechas
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,50)
    localfisico.realizar_compra(100,100)
    localfisico.realizar_compra(99,50)
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    assert localfisico.valor_ventas_del_dia() == 675000


####################### Ejercicio 9 #######################

def test_cuatro_ventas_dos_de_este_año_debe_devovler_dos_ventas_del_anio():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,50)
    localfisico.realizar_compra(100,100)
    localfisico.realizar_compra(99,50)
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    assert len(localfisico.ventas_del_anio()) == 2


####################### Ejercicio 10 #######################

def test_tres_productos_mas_vendidos_debe_devolver_los_nombres_de_los_tres_productos_mas_vendidos_en_orden_ascendente():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(pantalon_m)
    localfisico.registrar_producto(campera_l)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(remera_m)
    recargar_stock_a_cinco_productos()
    realizar_compra_a_cinco_productos()
    assert localfisico.productos_mas_vendidos(3)  == ["pantalon talle m", "campera talle l", "pulserita de tela verde"]


####################### Actualizaciones de precio segun criterios #######################

def test_act_precio_por_categoria_accesorios_en_un_50_porciento_devuelve_un_precio_de_75():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(pulsera)
    localfisico.actualizar_precio_segun(PorCategoria("  AcceSorios"),50)
    assert pulsera.precio == 75

def test_act_precio_por_nombre_remera_en_un_50_porciento_devuelve_un_precio_de_6750():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.actualizar_precio_segun(PorNombre("remera talle m"),50)
    assert remera_m.precio == 6750

def test_act_precio_de_un_producto_en_un_50_porciento_si_su_valor_es_menor_a_5000():
    localfisico.reiniciar_listas()
    reiniciar_precio_y_stocks_de_poductos()
    registrar_cinco_productos()
    localfisico.actualizar_precio_segun(PorPrecio(5000),50)
    assert remera_m.precio == 6750
    assert remera_s.precio == 6750
    assert pulsera.precio == 75

def test_act_precio_de_productos_que_tengan_stock():
    localfisico.reiniciar_listas()
    reiniciar_precio_y_stocks_de_poductos()
    registrar_cinco_productos()
    recargar_stock_a_tres_productos()
    localfisico.actualizar_precio_segun(PorStock(),50)
    assert remera_m.stock == 100
    assert remera_m.precio == 6750
    assert pulsera.precio == 75
    assert remera_s.precio == 6750

def test_act_precio_por_opcion_de_criterio_stock_en_un_50_porciento():
    localfisico.reiniciar_listas()
    registrar_cinco_productos()
    recargar_stock_a_tres_productos()
    localfisico.actualizar_precio_segun(PorOposicion(PorStock()),50)
    assert campera_l.precio == 52500
    assert pantalon_m.precio == 9000





############# Ganancias de Sucursal Fisica #############

def test_ganancia_del_dia_devuelve_4000000():
    localfisico.reiniciar_listas()
    compra_fisica_200()
    assert localfisico.ganancia_diaria() == 4000000



############# Ganancias de Sucursal Virtual #############


def test_ganancia_del_dia_si_se_realizan_200_ventas_devuelve_2075000():
    localvirtual.reiniciar_listas()
    compra_virtual_de_200_ventas()
    assert localvirtual.ganancia_diaria() == 2075000


def test_ganancia_del_dia_si_se_realizan_50_ventas_devuelve_1017500():
    localvirtual.reiniciar_listas()
    compra_virtual_de_50_unidades()
    assert localvirtual.ganancia_diaria() == 1017500
