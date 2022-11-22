from flask import Flask, request, render_template, url_for
from local import *
from prenda import *

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")
    

@app.get("/listadodeproductos")
def listado_productos():
    p = localfisico.ver_productos()
    return render_template("listadodeproductos.html", p=p)    

@app.get("/detalledeproducto")
def detalle():
    return render_template("detalledeproducto.html")


@app.get("/listadodeventas")
def ventas():
    nombre = request.form.get("nombre")
    return render_template("listadodeventas.html")
