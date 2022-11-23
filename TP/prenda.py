from criterios import *


class Prenda:
    def __init__(self,codigo,nombre,categoria,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.categorias=[categoria]
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
        return str(self.categorias)
    def stock_(self):
        return int(self.stock)
        
    def recarga_stock(self,stock):
        self.stock+=stock

    def restar_stock(self,stock):
        self.stock-=stock

    def hay_stock(self):
        return self.stock > 0
    
    def es_de_categoria(self,categoria):
        return categoria in self.categorias
    
    def agregar_categoria(self,categoria):
        self.categorias.append(categoria)

    def es_de_nombre(self,name):
        return self.nombre==name
    
    def es_de_precio(self,valor):
        return self.precio <= valor
    # def es_precio_menor_a(self,precio):
    #     return self.precio < precio

    def actualizar_precio(self,valor):
        self.precio += self.precio * valor / 100
        

    def cambiar_estado(self,estado_nuevo):
        self.estado = estado_nuevo
        self.precio = self.estado.precio(self.precio)


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



remera_m = Prenda(100,"remera talle m", "remera", 4500)
pulsera = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s = Prenda(99,"remera de talle s", "remera", 4500)
campera_l = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v2 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v2 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v2 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v2 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v2 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v2 = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v3 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v3 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v3 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v3 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v3 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v3 = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v4 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v4 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v4 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v4 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v4 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v4 = Prenda(333,"buzo talle m", "buzo", 5500)

remera_m_v5 = Prenda(100,"remera talle m", "remera", 4500)
pulsera_v5 = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s_v5 = Prenda(99,"remera de talle s", "remera", 4500)
campera_l_v5 = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m_v5 = Prenda(444,"pantalon talle m", "pantalon", 6000)
buzo_m_v5 = Prenda(333,"buzo talle m", "buzo", 5500)





promo_500 = Promocion(500)
promo_300=Promocion(300)
liquidacion=Liquidacion()
nueva=Nueva()