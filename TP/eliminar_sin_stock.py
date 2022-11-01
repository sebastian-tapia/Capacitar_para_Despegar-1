from tp_macowins import *
from datetime import datetime



def main():
    print(datetime.now(), "Eliminando productos sin stock")
    localfisico.discontinuar_productos()
    localvirtual.discontinuar_productos()
    print(datetime.now(), "Productos sin stock eliminados")
if __name__ == "__main__":
    main()



