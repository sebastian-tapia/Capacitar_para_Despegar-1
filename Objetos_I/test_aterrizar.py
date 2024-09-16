from aterrizar import *

ro = None
ana = None
a48 = None

def setup_function():
    global ro
    global ana
    global a48
    ro = Cliente()
    ana = Cliente()
    a48 = Asieno()

def test_a48_puede_venderse_a_ro():
    a48.venderse(ro)
    assert not a48.vendido_a(ro)
    assert not a48.esta_vendido()