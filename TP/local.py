import csv
from prenda import *
from criterios import *
from datetime import date
hoy = date.strftime(date.today(), "%Y-%m-%d")
from operator import itemgetter


class Local:
    def __init__(self):
        self.productos=[]
        self.ventas=[]
        self.codigos=[]
        self.reporte = ["Fecha", "Cantidad de Ventas", "Valor Ventas del día"]

        
    def ver_productos(self):
        productos_2 = []
        for producto in self.productos:
            productos_2.append( producto.detalle())
        return productos_2


    def reiniciar_listas(self):
        self.productos.clear()
        self.ventas.clear()
        self.codigos.clear()
        #self.criterio=PorCategoria()

    def registrar_producto(self,objeto):  
            if  objeto.codigo_() in self.codigos:
                raise ValueError("Producto ya registrado")
            else:
                self.productos.append(objeto)
                self.codigos.append(objeto.codigo_())
    
    def recargar_stock(self,codigo,cantidad):
        #if codigo in self.codigos:    
            for producto in self.productos:    
                if producto.codigo == codigo:
                    producto.recarga_stock(cantidad)
        #else:
        #    raise ValueError("El producto no esta registrado")

    def contar_categorias(self):
        categorias = []
        for producto in self.productos: 
            if producto.categoria_() not in categorias:
                categorias.append(producto.categoria_())
        return len(categorias) 

    def realizar_compra(self,codigo_de_producto, cantidad_de_items_a_comprar):
        for producto in self.productos:
            if producto.codigo_() == codigo_de_producto and cantidad_de_items_a_comprar > 0:
                producto.restar_stock(cantidad_de_items_a_comprar)
                if producto.stock_() < 0:
                    raise ValueError('No hay stock suficiente para la venta')   
                else:
                    
                    venta = {
                    "codigo_producto": producto.codigo_(),
                    "cantidad": cantidad_de_items_a_comprar,
                    "fecha": hoy,
                    "precio_total": producto.precio_() * cantidad_de_items_a_comprar
                    }
                    self.ventas.append(venta)

    def discontinuar_productos(self):
        for producto in list(self.productos):
            if not producto.hay_stock():
                self.productos.remove(producto)
                self.codigos.remove(producto.codigo_())


    def ventas_del_dia(self):
        ventas = 0
        for venta in self.ventas:
            if venta["fecha"] == hoy:
                ventas += 1
        return ventas

    def valor_ventas_del_dia(self):
        total_ventas_del_dia = 0
        subtotal = 0
        for venta_de_hoy in self.ventas:
            if venta_de_hoy["fecha"] == hoy:
                subtotal = venta_de_hoy["precio_total"] #* venta_de_hoy["cantidad"]
                total_ventas_del_dia += subtotal
        return total_ventas_del_dia

    def cantidad_ventas_del_dia(self):
        cantidad = 0
        for venta_de_hoy in self.ventas:
            if venta_de_hoy["fecha"] == hoy:
                subtotal = venta_de_hoy["cantidad"]
                cantidad += subtotal
        return cantidad

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
                if producto.codigo_() == producto_venta["codigo_producto"]:
                    producto_y_cantidad = {
                        "nombre": producto.nombre_(),
                        "cantidad": producto_venta["cantidad"]
                    }
                    lista_mas_vendidos.append(producto_y_cantidad)
        ventas_ordenadas_may_a_menor = sorted(lista_mas_vendidos, key=itemgetter("cantidad"), reverse=True)
        for producto in ventas_ordenadas_may_a_menor:
            if producto["nombre"] not in nombres_mas_vendidos:
                nombres_mas_vendidos.append(producto["nombre"])
        return nombres_mas_vendidos[:cantidad]


    def actualizar_precio_segun(self,criterio,valor):
        for producto in self.productos:
            if criterio.aplica_a(producto):
                producto.actualizar_precio(valor)
    
    
    def listar_por(self,criterio):
        return [ producto for producto in self.productos if criterio.aplica_a(producto)]


    def productos_sin_stock(self):
        cont = 0
        for producto in self.productos:
            if producto.stock == 0:
                cont += 1
        return cont

    def reporte_diario(self):
        self.reporte.append([hoy, self.cantidad_ventas_del_dia(), self.valor_ventas_del_dia()])
        with open("reporte.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.reporte)
    
    def buscar(self,busqueda):
        prod_encontrados = []
        for producto in self.productos:
            if type(busqueda) == int:
                if producto.es_de_precio(busqueda):
                        prod_encontrados.append(producto.detalle())    
            else:
                if producto.es_de_nombre(busqueda):
                    prod_encontrados.append(producto.detalle())
                elif producto.es_de_categoria(busqueda):
                    prod_encontrados.append(producto.detalle())
        return prod_encontrados        
                

            

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








local=Local()
localvirtual = Virtual(10000)
localfisico = Fisico(75000)
local_retiro = Fisico(75000)
local_monserrat = Fisico(75000)
local_florida = Fisico(75000)

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
liquidacion = Liquidacion()
nueva = Nueva()




local_retiro.registrar_producto(remera_m)
local_retiro.registrar_producto(pulsera)
local_retiro.registrar_producto(remera_s)
local_retiro.registrar_producto(campera_l)
local_retiro.registrar_producto(pantalon_m)
local_retiro.registrar_producto(buzo_m)
local_retiro.recargar_stock(100,100)
local_retiro.recargar_stock(1098,100)
local_retiro.recargar_stock(99,100)
local_retiro.realizar_compra(100,50)
local_retiro.realizar_compra(1098,10)
local_retiro.realizar_compra(99,10)


