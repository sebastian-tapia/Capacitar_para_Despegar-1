from flask import Flask, request, render_template, url_for, redirect
from local import *
from prenda import *

app = Flask(__name__)



@app.route("/")
def raiz():
    p = local_retiro.ver_productos()
    return render_template("home.html", p=p)

@app.route("/resultado", methods=['GET','POST','DELETE'])
def resultado():
    busqueda = request.form.get('busqueda')
    r = local_retiro.buscar(busqueda)
    return render_template("resultado.html", r=r, busqueda=busqueda)



@app.get("/listadodeproductos")   
def listado_productos():
    p = local_retiro.ver_productos()
    return render_template("listadodeproductos.html", p=p)    

@app.route("/detalledeproducto", methods=['GET','POST','DELETE'])
def detalle():
    producto = local_retiro.ver_productos()
    return render_template("detalledeproducto.html", producto=producto)


@app.get("/listadodeventas")
def ventas():
    # lista_de_ventas = local_retiro.ventas()
    return render_template("listadodeventas.html")

