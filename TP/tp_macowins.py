#from curses import ncurses_version
from logging.config import dictConfig
from operator import itemgetter
import re
from shutil import register_archive_format
from subprocess import getstatusoutput
from xml.dom import registerDOMImplementation
from datetime import date
hoy = date.strftime(date.today(), "%Y-%m-%d")





remera_talle_m = {
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": ["remera"],
    "precio": 4500
}

pulserita = {
    "codigo": 1098,
    "nombre": "pulserita de tela verde",
    "categoria": ["accesorios"],
    "precio": 50
}

remera_talle_s = {
    "codigo": 99,
    "nombre": "remera talle s",
    "categoria": ["remera"],
    "precio": 4500
}

campera_talle_l = {
    "codigo": 555,
    "nombre": "campera talle l",
    "categoria": ["campera"],
    "precio": 44500
}

pantalon_talle_m = {
    "codigo": 444,
    "nombre": "pantalon talle m",
    "categoria": ["pantalon"],
    "precio": 6000
}

class Local:
    def __init__(self):
        self.productos=[]
        self.codigos=[]
        self.ventas=[]

    def reiniciar_listas(self):
        self.productos.clear()
        self.ventas.clear()
        self.codigos.clear()

    def registrar_producto(self,producto):  
        if  producto.codigo in self.codigos:
            raise ValueError("Producto ya registrado")
        else:
            self.productos.append(producto.producto)
            self.codigos.append(producto.codigo)


    def recargar_stock(self,codigo,stock):
        if codigo not in self.codigos:
            raise ValueError("Codigo de producto ingresado no existe")
        else:
            for producto in self.productos:
                if producto["codigo"] == codigo:
                    producto["stock"] += stock


    def hay_stock(self,codigo):
        for producto in self.productos:
            if producto["codigo"] == codigo and producto["stock"] > 0:
                return True
        return False


    def contar_categorias(self):
        categorias = []
        for producto in self.productos: 
            if producto["categorias"] not in categorias:
                categorias.append(producto["categorias"])
        return len(categorias) 


    def realizar_compra(self,codigo_de_producto, cantidad_de_items_a_comprar):
        for producto in self.productos:
            if producto["codigo"] == codigo_de_producto and cantidad_de_items_a_comprar > 0:
                hay_stock_para_vender = producto["stock"] - cantidad_de_items_a_comprar
                if hay_stock_para_vender < 0:
                    raise ValueError('No hay stock suficiente para la venta')   
                else:
                    producto["stock"] = hay_stock_para_vender
                    venta = {
                    "codigo_producto": producto["codigo"],
                    "cantidad": cantidad_de_items_a_comprar,
                    "fecha": hoy,
                    "precio_total": producto["precio"] * cantidad_de_items_a_comprar
                    }
                    self.ventas.append(venta)


    def discontinuar_productos(self):
        dic_aux = self.productos[:]
        for producto in dic_aux:
            if producto["stock"] == 0:
                self.productos.remove(producto)
                self.codigos.remove(producto["codigo"])

        for producto in self.productos:
            if producto["stock"] == 0:
                self.productos.remove(producto)
                self.codigos.remove(producto["codigo"])


    def ventas_del_dia(self):
        ventas = 0
        for venta in self.ventas:
            if venta["fecha"] == hoy:
                ventas += 1
        return ventas

    def cantidad_ventas_del_dia(self):
        cantidad = 0
        for venta_de_hoy in self.ventas:
            if venta_de_hoy["fecha"] == hoy:
                subtotal = venta_de_hoy["cantidad"]
                cantidad += subtotal
        return cantidad

    def valor_ventas_del_dia(self):
        total_ventas_del_dia = 0
        subtotal = 0
        for venta_de_hoy in self.ventas:
            if venta_de_hoy["fecha"] == hoy:
                subtotal = venta_de_hoy["precio_total"] #* venta_de_hoy["cantidad"]
                total_ventas_del_dia += subtotal
        return total_ventas_del_dia

    def ventas_del_anio(self):
        ventas_del_anio_actual = []
        anio_actual = hoy[:4]
        for producto in self.ventas:
            if producto["fecha"][:4] == anio_actual:
                ventas_del_anio_actual.append(producto)
        return ventas_del_anio_actual

    def productos_mas_vendidos(self,cantidad):
        lista_mas_vendidos = []
        nombres_mas_vendidos = []
        for producto_venta in self.ventas:
            for producto in self.productos:
                if producto["codigo"] == producto_venta["codigo_producto"]:
                    producto_y_cantidad = {
                        "nombre": producto["nombre"],
                        "cantidad": producto_venta["cantidad"]
                    }
                    lista_mas_vendidos.append(producto_y_cantidad)
        ventas_ordenadas_may_a_menor = sorted(lista_mas_vendidos, key=itemgetter("cantidad"), reverse=True)
        for producto in ventas_ordenadas_may_a_menor:
            if producto["nombre"] not in nombres_mas_vendidos:
                nombres_mas_vendidos.append(producto["nombre"])
        return nombres_mas_vendidos[:cantidad]


    def actualizar_precios_por_categoria(self,categoria,porcentaje):
        categoria_reconocida = categoria.lower().strip()
        for producto in self.productos:
            if categoria_reconocida in producto["categorias"]:
                producto["precio"] += producto["precio"] * porcentaje / 100

#AQUI?
    def busqueda_categoria(self,categoria):
        categoria_encontrada = True
        categoria_reconocida = categoria.lower().strip()
        for producto in self.productos:
            if categoria_reconocida in producto["categoria"]:
                return categoria_encontrada

    def actualizar_precio_por_nombre(self,nombre_categoria,porcentaje):
        busqueda_reconocida = nombre_categoria.lower().strip()
        for producto in self.productos:
            if re.search(busqueda_reconocida, producto["nombre"], re.IGNORECASE):
                producto["precio"] += producto["precio"] * porcentaje / 100


    def stock_por_codigo(self,codigo):
        stock = 0
        for i in self.productos:
            if i["codigo"] == codigo:
                stock = i["stock"]
        return stock


class Fisico(Local):
    def __init__(self,gasto_fijo):
        super().__init__()
        self.gasto_fijo = gasto_fijo
        
    def ganancia_diaria(self):
        return self.valor_ventas_del_dia() - self.gasto_fijo


class Virtual(Local):
    def __init__(self,gasto_variable):
        super().__init__()
        self.gasto_variable = gasto_variable

    def gasto_por_ventas_diarias(self):
        if self.ventas_del_dia() > 100:
            return self.cantidad_ventas_del_dia() * self.gasto_variable
        else:
            return 0
        
    def ganancia_diaria(self):
        return self.valor_ventas_del_dia() - self.gasto_por_ventas_diarias()


class Prenda:
    def __init__(self,codigo,nombre,categorias,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categorias = [categorias]
        self.precio = precio
        self.stock = 0
        self.estado = Nueva()

        self.producto = {   "codigo": self.codigo,
                            "nombre": self.nombre,
                            "categorias": self.categorias,
                            "precio": self.precio,
                            "stock": self.stock}

    def cambiar_estado(self,estado_nuevo):
        self.estado = estado_nuevo


    def precio_estado(self):
        return self.estado.precio(self.precio)


    # def calcular_precio_final(self, es_extranjero):
    #     if self.diccionario["precio"] > 70 and es_extranjero:
    #         return self.diccionario["precio"]
    #     else:
    #         costo_final = self.diccionario["precio"] * 1.21
    #         return costo_final

    def categoria(self,busquedaCategoria):
        categoria_reconocida = busquedaCategoria.lower().strip()
        return categoria_reconocida in self.categorias

    def agregar_categoria(self,nuevaCategoria):
        self.producto["categorias"].append(nuevaCategoria)

    def actualizar_precio_por_nombre(self,busqueda,porcentaje):
        busqueda_reconocida = busqueda.lower().strip()
        if re.search(busqueda_reconocida, self.nombre, re.IGNORECASE):
            self.precio += self.precio * porcentaje / 100
            return self.precio



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


localvirtual = Virtual(1000)
localfisico = Fisico(77500)
remera_m = Prenda(100,"remera talle m", "remera", 4500)
pulsera = Prenda(1098,"pulserita de tela verde", "accesorios", 50)
remera_s = Prenda(99,"remera de talle s", "remera", 4500)
campera_l = Prenda(555,"campera talle l", "campera", 35000)
pantalon_m = Prenda(444,"pantalon talle m", "pantalon", 6000)
promo_500 = Promocion(500)
liquidacion = Liquidacion()
nueva = Nueva()




