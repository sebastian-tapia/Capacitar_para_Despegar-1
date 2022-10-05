from tp_macowins import *

def test_suma():
    assert suma(2, 2) == 4

@pytest.mark.parametrize(
    ("input_x", "expected"),
    (
        ({"codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500},{"codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500,"stock":0}),
        #(1,2),
    ),
)

def test_registrar_producto(input_x):
    
    # productos = []
    # codigos = []
    # if input_x["codigo"] in codigos:
    #     raise  ValueError("Producto ya registrado")
    # else:
    #     input_x["stock"] = 0
    #     productos.append(input_x)
    #     codigos.append(input_x["codigo"]) 
    productos = []
    assert registrar_producto(
    
    #codigos = []
    if input_x["codigo"] in codigos:
        raise  ValueError("Producto ya registrado")
    else:
        productos["stock"] = 0
        productos.append(input_x)
        codigos.append(input_x["codigo"])) == expected
