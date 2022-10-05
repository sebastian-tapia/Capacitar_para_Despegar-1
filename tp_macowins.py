from operator import itemgetter
from datetime import date

def suma(a,b):
    return a + b

hoy = date.strftime(date.today(), "%Y-%m-%d")
#ventas = []
productos = []
codigos = []


remera_talle_m = {
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500
}

pulserita = {
    "codigo": 1098,
    "nombre": "pulserita de tela verde",
    "categoria": "accesorios",
    "precio": 50
}

remera_talle_s = {
    "codigo": 99,
    "nombre": "remera talle s",
    "categoria": "remera",
    "precio": 4500
}

campera_talle_l = {
    "codigo": 555,
    "nombre": "campera talle l",
    "categoria": "campera",
    "precio": 44500
}

pantalon_talle_m = {
    "codigo": 444,
    "nombre": "pantalon talle m",
    "categoria": "pantalon",
    "precio": 6000
}




# 1. Registrar_producto: recibe un diccionario con codigo, nombre, categoria, precio y agrega un producto nuevo a la lista de productos. El stock del producto agregado debe estar inicialmente en cero.


def registrar_producto(nombre_producto):
    global productos
    global codigos
    if nombre_producto["codigo"] in codigos:
        raise  ValueError("Producto ya registrado")
    else:
        nombre_producto["stock"] = 0
        productos.append(nombre_producto)
        codigos.append(nombre_producto["codigo"])



# 2. recargar_stock: toma un código de producto y una cantidad de unidad de stock a agregar, e incrementa el stock correspondiente a ese producto. Si el código de producto indicado no existe, debe lanzar una excepción. 


def recargar_stock(codigo,stock):
    global productos
    if codigo not in codigos:
        raise ValueError("Codigo de producto ingresado no existe")
    else:
        for producto in productos:
            if producto["codigo"] == codigo:
                producto["stock"] += stock





# 3. hay_stock: recibe un código de producto y dice si hay stock (es decir, si el stock correspondiente es mayor a cero). Si el código indicado no existe en la lista de productos, debe devolver False.

def hay_stock(codigo):
    for producto in productos:
        if producto["codigo"] == codigo and producto["stock"] > 0:
            return "Hay stock de " + str(producto["stock"]) + " " + producto["nombre"]
        elif producto["codigo"] == codigo and producto["stock"] <= 0 :
            return "No hay stock de " + producto["nombre"]
    return False




#  4. calcular_precio_final: toma un producto (un diccionario) y un booleano es_extranjero y calcula su valor final, según la siguiente regla:
#   a. si quien calcula el precio es extranjero y el valor es mayor de $70, es el mismo valor sin cambios. 
# b. en caso contrario, es el valor original más un 21%

def calcular_precio_final(producto, es_extranjero):
    if es_extranjero and producto["precio"] > 70:
        return producto["precio"]
    else:
        costo_final = producto["precio"] * 1.21
        return costo_final




# 5. contar_categorias: retorna la cantidad de categorías únicas

def contar_categorias(productos):
    categorias = []
    for producto in productos: 
        if producto["categoria"] not in categorias:
            categorias.append(producto["categoria"])
    return "Hay " + str(len(categorias)) + " categorias"



# 6. realizar_compra: recibe un código de producto y una cantidad de items a comprar. En base a ello, decrementa el stock del producto correspondiente y crea una nueva venta con la información correspondiente. Si no hay suficiente stock, lanzar una excepción.

def realizar_compra(codigo_de_producto, cantidad_de_items_a_comprar):
    global ventas
    global productos
    for producto in productos:
        if producto["codigo"] == codigo_de_producto:
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
                ventas.append(venta)
                return "Compra realizada, agregada a ventas"
        # else:
        #     return "Código incorrecto o cantidad de items no puede ser menor a 1"




# 7. discontinuar_productos: elimina los productos sin stock.

def discontinuar_productos(dic_productos):
    global productos
    dic_aux = dic_productos[:]
    for producto in dic_aux:
        if producto["stock"] == 0:
            dic_productos.remove(producto)
    return dic_productos



# 8. valor_ventas_del_dia: retorna el valor total de las ventas del día de hoy
#en el diccionario ventas, en el ejercicio 6, se cambio la clave precio por precio total, por eso en esta funcion ya no se multiplica por cantidad


def valor_ventas_del_dia():
    suma_ventas_del_dia = 0
    subtotal = 0
    for venta_de_hoy in ventas:
        if venta_de_hoy["fecha"] == hoy:
            subtotal = venta_de_hoy["precio_total"] #* venta_de_hoy["cantidad"]
            suma_ventas_del_dia += subtotal
    return "El valor total de ventas de hoy es de: $" + str(suma_ventas_del_dia)





# 9. ventas_del_anio: retorna un listado con todas las ventas para el año actual.

def ventas_del_anio():
    ventas_del_anio = []
    anio = hoy[:4]
    for producto in ventas:
        if producto["fecha"][:4] == anio:
            ventas_del_anio.append(producto)
    return ventas_del_anio



# 10. productos_mas_vendidos: toma una cantidad n de productos y retorna los nombres de los n productos más vendidos

def productos_mas_vendidos(cantidad):
    lista_mas_vendidos = []
    nombres_mas_vendidos = []
    for producto_venta in ventas:
        for producto in productos:
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



# 11. actualizar_precios_por_categoria: toma una categoría y un porcentaje, y actualiza según ese porcentaje el precio de todos los productos que tengan esa categoría. La búsqueda de categoría en este procedimiento no debe ser exacta: por ejemplo tanto si se pasa como argumento "REMERA", " REMERA" o "Remera", deben actualizarse los productos de la categoría "remera".

def actualizar_precios_por_categoria(categoria,porcentaje):
    global productos
    categoria_reconocida = categoria.lower().strip()
    count = 0
    for producto in productos:
        if producto["categoria"] == categoria_reconocida:
            producto["precio"] += producto["precio"] * porcentaje / 100
        else:
            count += 1
# estara bien el raise acá, preguntar en clase            
    if count == len(productos):
        raise ValueError("Categoria no encontrada o mal escrita")

## Agregado el miércoles