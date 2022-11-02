import pickle, glob

def guardar(nombre, elemento):
  with open(f"{nombre}.pickle", "wb") as f:
    pickle.dump(elemento, f)

def cargar(nombre):
  with open(f"{nombre}.pickle", "rb") as f:
    return pickle.load(f)

def cargar_todos():
  elementos = {}
  for path in glob.glob("*.pickle"):
    nombre = path.replace(".pickle", "")
    elementos[nombre] = cargar(nombre)

  return elementos