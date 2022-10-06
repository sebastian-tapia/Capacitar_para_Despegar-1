class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia = self.energia + 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia < 10

  def esta_feliz(self):#probar energia
    return self.energia > 500
  

  def __repr__(self) -> str:
    return f"<🐦 at {hex(id(self))}>"

class Dragon:
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10  

  def esta_debil(self):
    return self.energia < 50

  def esta_feliz(self):#probar energia
    return self.energia > 500

  def __repr__(self) -> str:
    return f"<🔥 at {hex(id(self))}>"


class Entrenador:
    def entrenar(self,animal):
        animal.volar_en_circulos()


maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = Entrenador(animal)