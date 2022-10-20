from TP3 import *
import pytest


####################### EJERCICIO 1 #######################
def test_se_agregra_productos_a_lista_():
    localfisico = Fisico(3250)
    localfisico.registrar_producto(remera_m)
    assert len(localfisico.productos)==1
def test_se_agregra_productos_repetido_se_espera_el_RAISE_exception():
    localfisico = Fisico(3250)
    localfisico.reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:

        localfisico.registrar_producto(pulsera)
        localfisico.registrar_producto(pulsera)
        
    assert str(auxiliar.value) == "Producto ya registrado"

def test_al_REGISTRAR_producto_se_espera_que_ingrese_con_stock_en_0():

    localfisico = Fisico(3250)
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(pulsera)
    assert localfisico.buscar_prenda_por_codigo_devoler_stock(1098)==0
    
def test_registro_2_productos_se_espera_que_productos_tenga_2():
    localfisico = Fisico(3250)
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(remera_m)
    assert len(localfisico.productos) ==2


####################### EJERCICIO 2 #######################

def test_recarga_stock_20_a_un_producto_devuelve_20():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,20)
    assert localfisico.buscar_prenda_por_codigo_devoler_stock(100)==20

def test_cargar_stock_con_codigo_inexistente_en_productos_devuelve_exepcion():
    localfisico.reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        localfisico.recargar_stock(1000,10)
    assert str(auxiliar.value) == "Codigo de producto ingresado no existe"
    assert len(localfisico.productos)==0



####################### EJERCICIO 3 #######################

def test_no_hay_stock_en_un_producto_recien_registrado_deberia_dar_false_():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    assert not localfisico.hay_stock(100)

def test_cargar_stock_a_un_producto_registrado_y_preguntar_si_tiene_stock_devuelve_True_():
    localfisico = Fisico(3250)
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,100)
    assert localfisico.hay_stock(100)



# def test_foo():
#     remera_m=Prenda(remera_talle_m)
#     assert remera_m.diccionario==remera_talle_m
#     print(remera_m.diccionario)

####################### EJERCICIO 4 #######################

def test_precio_final_remera_m_y_sea_turista_es_4500():
    assert remera_m.calcular_precio_final(True)==4500

def test_precio_final_pulserita_y_no_sea_turista_es_60_5():
    assert pulsera.calcular_precio_final(False)==60.5


####################### EJERCICIO 5 #######################

def test_agrego_2_productos_distintas_categorias_deberia_devolver_2():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(pulsera)
    assert localfisico.contar_categorias()==2

def test_registrar_2_productos_misma_categoria_devuelve_1():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    assert localfisico.contar_categorias()==1


####################### EJERCICIO 6 #######################

def test_realizar_una_compra_de_un_producto_decrementa_su_stock_de_100_a_80():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,100)
    localfisico.realizar_compra(100,20)
    assert localfisico.buscar_prenda_por_codigo_devoler_stock(100)==80


def test_al_realizar_una_compra_se_agregar_el_producto_a_ventas_y_largo_de_ventas_es_1():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,100)
    localfisico.realizar_compra(100,20)
    assert len(localfisico.ventas)==1

def test_al_realizar_una_compra_se_agregar_el_producto_a_ventas_y_largo_de_ventas_es_2():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.recargar_stock(100,100)
    localfisico.realizar_compra(100,20)
    localfisico.realizar_compra(100,10)
    assert len(localfisico.ventas)==2


####################### EJERCICIO 7 #######################

def test_remueve_todos_los_productos_con_stock_en_0():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.discontinuar_productos()
    assert len(localfisico.productos)==0

def test_elimina_el_producto_sin_stock_de_tres_productos_la_lista_productos_debe_ser_2():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,50)
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


####################### EJERCICIO 8 #######################
# def valor_ventas_del_dia():
#     suma_ventas_del_dia = 0
#     subtotal = 0
#     for venta_de_hoy in ventas:
#         if venta_de_hoy["fecha"] == hoy:
#             subtotal = venta_de_hoy["precio_total"] #* venta_de_hoy["cantidad"]
#             suma_ventas_del_dia += subtotal
#     return suma_ventas_del_dia

def test_realizar_una_compra_del_dia_de_100_unidades_de_un_producto_que_cuesta_4500_debe_devolver_450000():
    localfisico.reiniciar_listas()
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,50)
    localfisico.realizar_compra(100,100)
    assert localfisico.valor_ventas_del_dia() == 450000

#a la lista de ventas se le agrega dos productos comprados con otras fechas
def test_ventas_del_dia_de_150_unidades_entre_dos_productos_debe_devolver_675000():
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


####################### EJERCICIO 9 #######################

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


####################### EJERCICIO 10 #######################

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


####################### EJERCICIO 11 #######################

def test_en_una_lista_de_cinco_productos_actualizar_precio_a_categoria_remera_mal_escrita_en_un_50_porciento_debe_actualizar_el_precio_a_6750():
    localfisico.reiniciar_listas()
    registrar_cinco_productos()
    localfisico.actualizar_precios_por_categoria(" reMera ",50)
    assert localfisico.productos[0]["precio"] == 6750
    assert localfisico.productos[1]["precio"] == 6750


def test_actualizar_precio_a_categoria_accesorios_mal_escrita_en_50_porciento_debe_actualizar_el_precio_a_75():
    localfisico.reiniciar_listas()
    registrar_cinco_productos()
    localfisico.actualizar_precios_por_categoria(" aCceSoriOs",50)
    assert localfisico.productos[2]["precio"] == 75





############# Tests de Prenda #############

#arrastra el precio de categoria aplicado en los tests de los ejercicios si no se reinician sus valores
def test_de_prenda_en_promocion_descuenta_500_de_su_valor_quedando_en_4000():
    remera_s.reiniciar_valores()
    assert remera_s.promocion(500) == 4000

def test_de_prenda_al_cambiar_a_nueva_debe_retomar_su_valor_original_de_4500():
    remera_s.reiniciar_valores()
    remera_s.promocion(500) == 4000
    assert remera_s.nueva() == 4500

def test_de_prenda_en_liquidacion_debe_devolver_la_mitad_de_su_valor_2250():
    assert remera_s.liquidacion() == 2250

def test_agregar_una_categoria_mas_a_una_prenda_debe_devoler_largo_de_cetegoria_2():
    remera_s.reiniciar_valores()
    remera_s.agregar_categoria("remera de basquet")
    assert len(remera_s.categoria_producto()) == 2

def test_indica_si_la_categoria_dada_corresponde_a_la_prenda():
    remera_s.reiniciar_valores()
    assert remera_s.categoria(" remera") == True

def test_prenda_con_dos_categorias_se_busca_su_segunda_categoria_mal_escrita():
    remera_s.reiniciar_valores()
    remera_s.agregar_categoria("remera de basquet")
    assert remera_s.categoria(" REMera de BASqueT ") == True

def test_buscar_nombre_incompleto_de_un_prodcuto_y_actualizar_su_precio_en_50_porciento_debe_devolver_6750():
    remera_s.reiniciar_valores()
    assert remera_s.actualizar_precio_por_nombre(" rem",50) == 6750





############# Tests de Sucursal Fisica #############
#arrastra el precio de categoria aplicado en los tests de los ejercicios si no se reinician sus valores 
# valor ventas total 677500
def test_ganancia_del_dia_se_obtiene_de_la_diferencia_entre_valor_de_ventas_y_gasto_fijo():
    localfisico.reiniciar_listas()
    remera_m.reiniciar_valores()
    remera_s.reiniciar_valores()
    pulsera.reiniciar_valores()
    compra_fisica_de_200_unidades()
    assert localfisico.ganancia_diaria() == 600000



############# Tests de Sucursal Virtual #############

def test_ganancia_del_dia():
    localvirtual.reiniciar_listas()
    remera_m.reiniciar_valores()
    remera_s.reiniciar_valores()
    pulsera.reiniciar_valores()
    compra_virtual_de_200_ventas()
    assert localvirtual.ganancia_diaria() == 477500