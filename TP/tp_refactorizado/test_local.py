import pytest
from tp_refactorizado import *

################# ejercicio 1###############
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

#####################ejercicio 2##################

