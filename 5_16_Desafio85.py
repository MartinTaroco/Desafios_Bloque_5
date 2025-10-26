#Dado un conjunto de estudiantes y sus promedios, implementa una función que cree un árbol binario de búsqueda en el que los nodos representan los promedios de los estudiantes. Luego, implementa una función que recorra el árbol en inorden para mostrar los estudiantes en orden ascendente de rendimiento académico.
 

#No entendi (o no logre) cumplir con el desafio, en su lugar, hcie un porgrama dodne el nodo orignial es la nota limite entre la suficiencia o no, y agregue las notas mas pequeñas a la izuqierda y la mas grande a la derecha

class Nodo:
  def __init__(self, nombre, promedio):
    self.nombre = nombre
    self.promedio = promedio
    self.izq = None
    self.der = None
    
raizOrigen = Nodo("Limite", 6)   #Raiz origen, 


#Función recursiva para agregar a la izquierda
def insertar_izquierda(raiz,nombre, promedio):
  if raiz.izq is None:
    raiz.izq = Nodo(nombre,promedio)
  else:
    insertar_izquierda(raiz.izq, nombre, promedio)
    
#funcion recursiva para agegar a la derecha    
def insertar_derecha(raiz,nombre, promedio):
  if raiz.der is None:
    raiz.der = Nodo(nombre,promedio)
  else:
    insertar_derecha(raiz.der, nombre, promedio)
  
lista=[("Cilcano", 11),("pablo", 1) ,("Mengano",10), ("PEdro", 9 ), ("Miguel", 2)]


#Agregando  promedios
for nombre, nota in lista:
  if nota < raizOrigen.promedio:
    insertar_izquierda(raizOrigen, nombre, nota)
  if nota > raizOrigen.promedio:
    insertar_derecha(raizOrigen, nombre, nota)


def recorrerlos(raiz):
    if raiz:
        print(f"Estudiante: {raiz.nombre}, Promedio: {raiz.promedio}")
        recorrerlos(raiz.izq)
        recorrerlos(raiz.der)

recorrerlos(raizOrigen)