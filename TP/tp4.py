
from tp_macowins import *
import pytest

class PorPrecio:
    def corresponde_al_producto(self,productos,valor):
        for producto in productos:
            if  producto["precio"]<valor:
                producto["precio"]= valor
class PorStock:
    def corresponde_al_producto(self,productos,valor):
        for producto in productos:
            if producto["stock"]>0:
                producto["precio"]= valor
class PorOposicion:
    def corresponde_al_producto(self,productos,valor):
        for producto in productos:
            if producto["precio"]>valor and producto["stock"]==0:
                producto["precio"]=valor


        
