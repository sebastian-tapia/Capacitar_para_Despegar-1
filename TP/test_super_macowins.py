from math import prod
import re
from tp_macowins import *
import pytest

def test_prueba_de_todas_funciones_relacionadas():
    reiniciar_listas()
    registrar_producto(remera_talle_m)
    assert len(productos) == 1
    registrar_producto(pulserita)
    assert len(productos) == 2
    registrar_producto(remera_talle_s)
    assert len(productos) == 3
    with pytest.raises(ValueError) as auxiliar:
        registrar_producto(remera_talle_s)
    assert str(auxiliar.value) == "Producto ya registrado"
    recargar_stock(100,300)
    recargar_stock(1098,400)
    recargar_stock(99,500)
    assert productos[0]["stock"] == 300
    assert productos[1]["stock"] == 400
    assert productos[2]["stock"] == 500
    with pytest.raises(ValueError) as auxiliar:
        recargar_stock(9999,10)
    assert str(auxiliar.value) == "Codigo de producto ingresado no existe"