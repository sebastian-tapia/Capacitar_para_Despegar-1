from tp_macowins import *
from datetime import datetime
from persistencia import *
import subprocess

subprocess.call(["zenity", "--info",  '--title=Semana terminada', "--text=Se eliminaran los productos sin stock", "--display=:0"])


def main():
    print(datetime.now(), "Eliminando productos sin stock")
    localfisico.discontinuar_productos()
    localvirtual.discontinuar_productos()
    print(datetime.now(), "Productos sin stock eliminados")

if __name__ == "__main__":
    main()



