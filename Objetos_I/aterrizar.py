class Asiento:
    def __init__(self):
        self.comprador = None
        self.estado = Libre()
    
    def venderse(self, cliente):
        if not esta_vendido():
            self.comprador = cliente

    def vendido_a(self,cliente):
        return self.comprador == cliente
    
    def esta_vendido(self):
        return self.comprador is not None 

    



class Cliente:
    def __init__(self):
        self.opcion = Asiento()

    