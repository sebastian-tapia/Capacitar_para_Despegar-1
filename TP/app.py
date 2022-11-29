from flask import Flask, request, render_template, url_for, redirect
from local import *
from prenda import *

app = Flask(__name__)



@app.route("/")
def raiz():
    p = local_retiro.ver_productos()
    return render_template("home.html", p=p)

@app.get("/resultado")
def resultado():
    busqueda = request.args['busqueda']
    # convertir los datos de arriba a string
    r = local_retiro.buscar(busqueda)
    return render_template("resultado.html", r=r, busqueda=busqueda)



@app.get("/listadodeproductos")   
def listado_productos():
    p = local_retiro.ver_productos()
    return render_template("listadodeproductos.html", p=p)    

@app.get("/productos/<int:id>")
def detalle(id):
    print("Estamos buscando el producto", id)
    producto = local_retiro.ver_productos()
    return render_template("detalle.html", producto=producto, id=id)


@app.get("/ventas")
def ventas():
    vendidos = local_retiro.ventas
    return render_template("ventas.html", vendidos=vendidos)

@app.get("/filtro")
def filtro():
    vendidos = local_retiro.ventas
    resultado = request.args['resultado']
    resultado1 = request.args['resultado1']
    return render_template("filtro.html", vendidos=vendidos, resultado=resultado, resultado1=resultado1)