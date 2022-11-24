from flask import Flask, request, render_template, url_for, redirect
from local import *
from prenda import *

app = Flask(__name__)



@app.route("/", methods=['GET','POST','DELETE'])
def raiz():
    busqueda = request.form.get('busqueda')
    # busqueda2 = local_retiro.buscar(busqueda)
    return render_template("home.html", busqueda3=ingre())

def ingre():
    return request.args.get("busqueda")

@app.get("/listadodeproductos")   
def listado_productos():
    p = local_retiro.ver_productos()
    return render_template("listadodeproductos.html", p=p)    

@app.get("/detalledeproducto")
def detalle():
    p = local_retiro.ver_productos()
    return render_template("detalledeproducto.html", p=p)


@app.get("/listadodeventas")
def ventas():
    return render_template("listadodeventas.html")

