from clasePrenda import *
from criterios import *
from datetime import date
hoy = date.strftime(date.today(), "%Y-%m-%d")
class Local:
    def __init__(self):
        self.productos=[]
        self.ventas=[]
        self.codigos=[]


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
        dic_aux = self.productos[:]
        for producto in dic_aux:
            if producto.stock_() == 0:
                self.productos.remove(producto)
                self.codigos.remove(producto.codigo_())

        for producto in self.productos:
            if producto.stock_() == 0:
                self.productos.remove(producto)
                self.codigos.remove(producto.codigo_())
    





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