from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def hola_mundo():
    return render_template("saludo.html", nombre={request.args.get("nombre","mundo")})


# @app.get ("/")   #la raiz (ruta)
# def hola_mundo():
#     return f"""
#     <h1>hola {request.args.get("nombre","mundo")}!</h1>
#     <p>Comando para cambiar el puerto: <br><br> <code>flask --debug run --port 8080</code></p>
#     """

def despedida():
    return f"""
    <h1>hola {request.args.get("nombre","mundo")}!</h1>
    <p>Comando para cambiar el puerto: <br><br> <code>flask --debug run --port 8080</code></p>
    """

print("Iniciando servidor")


#hacer lo mismo con despedida
#hacer una funcion para request.arg para no repetir codigo