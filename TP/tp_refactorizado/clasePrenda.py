
class Prenda:
    def __init__(self,codigo,nombre,categoria,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        self.stock=0
        self.estado=Nueva()

    def restaurar_stock(self):
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
    
    def es_de_categoria(self,cate):
        return self.categoria==cate
    
    def es_de_nombre(self,name):
        return self.nombre==name

    def actualizar_precio_segun_porcentaje(self,porcentaje):
        self.precio+=self.precio * porcentaje / 100

    def cambiar_estado(self,estado_nuevo):
        self.estado = estado_nuevo
        self.precio=self.estado.precio(self.precio)

    def calcular_precio_final(self, es_extranjero):
        if self.precio > 70 and es_extranjero:
            return self.precio
        else:
            costo_final = self.precio* 1.21
            return costo_final

class Nueva:
    def precio(self,precio):
        return precio
class Promocion:
    def __init__(self, promo):
        self.promo = promo
    def precio(self,precio):
        return precio - self.promo
class Liquidacion:
    def precio(self,precio):
        return precio / 2


remera_m=Prenda(100,"remera m","remera",4500)
remera_s = Prenda(99,"remera de talle s", "remera", 4500)
pantalon_m = Prenda(444,"pantalon talle m", "pantalon", 6000)

promo_300=Promocion(300)
liquidacion=Liquidacion()
nueva=Nueva()