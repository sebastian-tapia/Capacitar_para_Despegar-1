from datetime import date
hoy = date.strftime(date.today(), "%Y-%m-%d")

class PorCategoria:
  def __init__(self, categoria):
    self.categoria = categoria

  def aplica_a(self, producto):
    
    return producto.es_de_categoria(self.categoria.lower().strip())

class PorNombre:
  def __init__(self, patron):
    self.patron = patron

  def aplica_a(self, producto):
    return producto.es_de_nombre(self.patron)


