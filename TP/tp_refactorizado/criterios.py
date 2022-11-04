
class PorCategoria:
    def __init__(self,expresion_de_nombre):
        self.nombre=expresion_de_nombre

    def corresponde(self,producto):
        busqueda_reconocida = self.nombre.lower().strip()
        return busqueda_reconocida==producto