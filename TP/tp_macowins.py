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
        self.codigo=[]
        self.ventas=[]

    def reiniciar_listas(self):
        self.productos.clear()
        self.ventas.clear()
        self.codigo.clear()

    def registrar_producto(self,objeto):  
        if  objeto.codigo_producto() in self.codigo:
            raise ValueError("Producto ya registrado")
        else:
            self.productos.append(objeto.descripcion_producto())
            #self.productos[0]["stock"]=0
            objeto.descripcion_producto().update({"stock":0})
            self.codigo.append(objeto.codigo_producto())


    def recargar_stock(self,codigo,stock):
        if codigo not in self.codigo:
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
            if producto["categoria"] not in categorias:
                categorias.append(producto["categoria"])
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
            if categoria_reconocida in producto["categoria"]:
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



    def buscar_prenda_por_codigo_devoler_stock(self,codigo):
        for i in self.productos:
            if i["codigo"]==codigo:
                return i["stock"]


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
    def __init__(self,diccionario):
        self.diccionario=diccionario
        self.codigo_original = self.diccionario["codigo"]
        self.nombre_original = self.diccionario["nombre"]
        self.categoria_original = self.diccionario["categoria"]
        self.precio_original = self.diccionario["precio"]

    def calcular_precio_final(self, es_extranjero):
        if self.diccionario["precio"] > 70 and es_extranjero:
            return self.diccionario["precio"]
        else:
            costo_final = self.diccionario["precio"] * 1.21
            return costo_final


    def nueva(self):
        self.diccionario["precio"] = self.precio_original
        return self.diccionario["precio"]

    def promocion(self,promo):
        self.diccionario["precio"] -= promo
        return self.diccionario["precio"]

    def liquidacion(self):
        self.diccionario["precio"] /= 2
        return self.diccionario["precio"]

    def categoria(self,busquedaCategoria):
        categoria_reconocida = busquedaCategoria.lower().strip()
        return categoria_reconocida in self.diccionario["categoria"]

    def agregar_categoria(self,nuevaCategoria):
        self.diccionario["categoria"].append(nuevaCategoria)

    def actualizar_precio_por_nombre(self,busqueda,porcentaje):
        busqueda_reconocida = busqueda.lower().strip()
        if re.search(busqueda_reconocida, self.diccionario["nombre"], re.IGNORECASE):
            self.diccionario["precio"] += self.diccionario["precio"] * porcentaje / 100
            return self.diccionario["precio"]


    def descripcion_producto(self):
        return self.diccionario
    def codigo_producto(self):
        return self.diccionario["codigo"]
    def nombre_producto(self):
        return self.diccionario["nombre"]
    def categoria_producto(self):
        return self.diccionario["categoria"]
    def precio_producto(self):
        return self.diccionario["precio"]
    def reiniciar_valores(self):
        self.diccionario["codigo"] = self.codigo_original
        self.diccionario["nombre"] = self.nombre_original
        self.diccionario["categoria"] = self.categoria_original
        self.diccionario["precio"] = self.precio_original




localvirtual = Virtual(1000)
localfisico = Fisico(77500)
remera_m=Prenda(remera_talle_m)
pulsera=Prenda(pulserita)
remera_s=Prenda(remera_talle_s)
campera_l=Prenda(campera_talle_l)
pantalon_m=Prenda(pantalon_talle_m)

def realizar_compra_a_cinco_productos():
    localfisico.realizar_compra(100,25)
    localfisico.realizar_compra(99,50)
    localfisico.realizar_compra(1098,100)
    localfisico.realizar_compra(555,150)
    localfisico.realizar_compra(444,200)

def recargar_stock_a_cinco_productos():
    localfisico.recargar_stock(100,200)
    localfisico.recargar_stock(99,200)
    localfisico.recargar_stock(1098,200)
    localfisico.recargar_stock(555,200)
    localfisico.recargar_stock(444,200)

def registrar_cinco_productos():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(remera_s)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(campera_l)
    localfisico.registrar_producto(pantalon_m)



def compra_fisico():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(remera_s)
    remera_s.agregar_categoria("remera de futbol")
    remera_m.agregar_categoria("remera de basquet")
    localfisico.recargar_stock(100,500)
    localfisico.recargar_stock(1098,1000)
    localfisico.recargar_stock(99,2000)
    localfisico.realizar_compra(99,4)
    localfisico.realizar_compra(1098,5)
    localfisico.realizar_compra(100,10)
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})


def compra_virtual():
    localvirtual.registrar_producto(remera_m)
    localvirtual.registrar_producto(pulsera)
    localvirtual.registrar_producto(remera_s)
    remera_s.agregar_categoria("remera de futbol")
    remera_m.agregar_categoria("remera de basquet")
    localvirtual.recargar_stock(100,500)
    localvirtual.recargar_stock(1098,1000)
    localvirtual.recargar_stock(99,2000)
    localvirtual.realizar_compra(99,4)
    localvirtual.realizar_compra(1098,5)
    localvirtual.realizar_compra(100,10)
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})

def compra_virtual_de_200_ventas():
    localvirtual.registrar_producto(remera_m)
    localvirtual.registrar_producto(pulsera)
    localvirtual.registrar_producto(remera_s)
    remera_s.agregar_categoria("remera de futbol")
    remera_m.agregar_categoria("remera de basquet")
    localvirtual.recargar_stock(100,500)
    localvirtual.recargar_stock(1098,1000)
    localvirtual.recargar_stock(99,2000)
    for i in range(100):
        localvirtual.realizar_compra(100,1) # 4500 * 100 = 450000 
    for i in range(50):
        localvirtual.realizar_compra(1098,1) # 50 * 50 = 2500        Total  677500
    for i in range(50):
        localvirtual.realizar_compra(99,1) # 4500 * 50 = 225000
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localvirtual.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localvirtual.ventas_del_dia()

def compra_fisica_de_200_unidades():
    localfisico.registrar_producto(remera_m)
    localfisico.registrar_producto(pulsera)
    localfisico.registrar_producto(remera_s)
    localfisico.recargar_stock(100,500)
    localfisico.recargar_stock(1098,1000)
    localfisico.recargar_stock(99,2000)
    for i in range(100):
        localfisico.realizar_compra(100,1) # 4500 * 100 = 450000 
    for i in range(50):
        localfisico.realizar_compra(1098,1) # 50 * 50 = 2500        Total  677500
    for i in range(50):
        localfisico.realizar_compra(99,1) # 4500 * 50 = 225000
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    localfisico.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    return localfisico.ventas_del_dia()