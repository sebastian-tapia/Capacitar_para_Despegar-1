########## Ejercicio 3 ##########
un_curso = [
  {
    'legajo': '123446',
    'nombre': 'María',
    'apellido': '(...)',
    'notas' : [10, 2, 3],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123450',
    'nombre': 'Carlos',
    'apellido': '(...)',
    'notas' : [5, 8, 8],
    'zona': 'CABA'
  },
  {
    'legajo': '123430',
    'nombre': 'Liz',
    'apellido': '(...)',
    'notas' : [4, 8, 2],
    'zona': 'CABA'
  },
  {
    'legajo': '123453',
    'nombre': 'Hector',
    'apellido': '(...)',
    'notas' : [9, 9, 1],
    'zona': 'Temperley'
  },
  {
    'legajo': '123110',
    'nombre': 'Ana',
    'apellido': '(...)',
    'notas' : [6, 7, 8],
    'zona': 'Quilmes'
  },
  {
    'legajo': '123371',
    'nombre': 'Ivana',
    'apellido': '(...)',
    'notas' : [7, 7, 9],
    'zona': 'Avellaneda'
  }
]

un_estudiante = {
    'legajo': '123371',
    'nombre': 'Ivana',
    'apellido': '(...)',
    'notas' : [7, 7, 9],
    'zona': 'Avellaneda'
  }

###############  3. Estadísticas del curso  ###############

def promedio(lista):
    return sum(lista)/len(lista)

#1.
def nota_final(un_estudiante):
    return promedio(un_estudiante["notas"])

#2.
def promedio_de_notas_del_curso(un_curso):
    notas_curso = 0
    for alumno in un_curso:
        #print(i["notas"])
        notas_curso += nota_final(alumno)
        promedio_final = notas_curso / len(un_curso) 
    return promedio_final

#3.
def estudiantes_aprobados(un_curso):
  aprobados = []
  for alumno in un_curso:
    if alumno["notas"][0] >= 4 and alumno["notas"][1] >= 4 and alumno["notas"][2] >= 4:
      aprobados.append(alumno)
  return aprobados


###############  4. Zonas y legajos  ###############

#1.
def cantidad_de_estudiantes_por_zona(un_curso):
  total_zonas = []
  for alumno in un_curso:
    total_zonas.append(alumno["zona"])
  zonas_limpias = list(set(total_zonas))
  diccionario_descuentos = {zona:0 for zona in zonas_limpias}
  print(diccionario_descuentos)