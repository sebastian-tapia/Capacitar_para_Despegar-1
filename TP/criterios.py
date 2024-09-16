from prenda import *

class PorCategoria:
    def __init__(self, categoria):
        self.categoria = categoria

    def aplica_a(self, producto):
        return producto.es_de_categoria(self.categoria.lower().strip())


class PorNombre:
    def __init__(self, patron):
      self.patron = patron

    def aplica_a(self, producto):
        return producto.es_de_nombre(self.patron)


class PorPrecio:
    def __init__(self,valor):
        self.valor = valor

    def aplica_a(self, producto):
        return  producto.precio < self.valor


class PorStock:

    def aplica_a(self, producto):
        return producto.stock > 0


class PorOposicion:
    def __init__(self,criterio):
        self.criterio = criterio

    def aplica_a(self, producto):
        return not (self.criterio.aplica_a(producto))