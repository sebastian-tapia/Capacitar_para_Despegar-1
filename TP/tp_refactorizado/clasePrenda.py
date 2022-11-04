
class Prenda:
    def __init__(self,codigo,nombre,categoria,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        self.stock=0
    def codigo_(self):
        return int(self.codigo)
    def nombre_(self):
        return str(self.nombre)
    def precio_(self):
        return int(self.precio)
    def categoria_(self):
        return str(self.categoria)
    def stock_(self):
        return int(self.stock)
        
    def recargar_stock(self,stock):
        self.stock+=stock
    def restar_stock(self,stock):
        self.stock-=stock
    def hay_stock(self):
        return not self.stock==0

    
remera_m=Prenda(100,"remera m","remera",4500)
remera_s = Prenda(99,"remera de talle s", "remera", 4500)
pantalon_m = Prenda(444,"pantalon talle m", "pantalon", 6000)