from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")


# @app.get ("/")   #la raiz (ruta)
# def hola_mundo():
#     return f"""
#     <h1>hola {request.args.get("nombre","mundo")}!</h1>
#     <p>Comando para cambiar el puerto: <br><br> <code>flask --debug run --port 8080</code></p>
#     """

@app.get("/saludo")
def saludo():
    return render_template("saludo.html")


@app.get("/recientes")
def recientes():
    return render_template("recientes.html")
    
    
    # f"""
    # <h1>hola {request.args.get("nombre","mundo")}!</h1>
    # <p>Comando para cambiar el puerto: <br><br> <code>flask --debug run --port 8080</code></p>
    # """

print("Iniciando servidor")


#hacer lo mismo con despedida
#hacer una funcion para request.arg para no repetir codigo