from local import *
from datetime import datetime
from persistencia import *
import subprocess

subprocess.call(["zenity", "--info",  '--title=Semana terminada', "--text=Se eliminaran los productos sin stock", "--display=:0"])


def main():
    print(datetime.now(), "Eliminando productos sin stock")
    guardar("ficheroExterno",localfisico.productos)
    print("Productos almacenados: " + str(len(localfisico.productos)))
    print("Productos sin stock: " + str(localfisico.productos_sin_stock()))
    localfisico.discontinuar_productos()
    cargar("ficheroExterno")
    cargar_todos()
    print("Productos disponibles: " +str(len(localfisico.productos)))
    print(datetime.now(), "Productos sin stock eliminados")

if __name__ == "__main__":
    main()



