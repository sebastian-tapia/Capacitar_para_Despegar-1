from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")

@app.get("/saludo")
def saludo():
    nombre = request.form.get("nombre")
    return render_template("saludo.html", nombre = nombre)


@app.get("/recientes")
def recientes():
    return render_template("recientes.html")