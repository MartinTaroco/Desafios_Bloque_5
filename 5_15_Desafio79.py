#Dado un conjunto de números enteros únicos, construye un árbol de búsqueda binaria (ABB) que inserte los valores de manera que el subárbol izquierdo de cada nodo contenga solo nodos con valores menores, y el subárbol derecho solo nodos con valores mayores. Una vez construido el árbol, implementa una función para buscar un número dado y devuelva si ese número existe en el árbol o no.class Nodo:
class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.izquierda = None
    self.derecha = None
    
def insertar_nodo(raiz,nodo):
  if raiz.valor is None:
     return Nodo(nodo)
  
  if nodo < raiz.valor:
      if raiz.izquierda is  None:
        raiz.izquierda = Nodo(nodo)
      else:
        insertar_nodo(raiz.izquierda, nodo)
  if nodo > raiz.valor:
    if raiz.derecha is None:
      raiz.derecha = Nodo(nodo)
    else:
      insertar_nodo(raiz.derecha, nodo)

lista_de_busqueda = []
def registro_nodos(nodo):

  if nodo:
    lista_de_busqueda.append(nodo.valor)
    registro_nodos(nodo.izquierda)
    registro_nodos(nodo.derecha)
  return lista_de_busqueda



def buscar_nodo(arbol, nodo):  
    if nodo in arbol:
      print("Esta si!!")
    else:
      print("No esta")
      
      
      
def pre_order(nodo):
 if nodo:
    print(nodo.valor, " ")
    pre_order(nodo.izquierda)
    pre_order(nodo.derecha)


raiz = Nodo(10)

lista_nodos = [2, 5, 20, 40, 5 , 3, 6]

for i in lista_nodos:
  insertar_nodo(raiz,i)
  
pre_order(raiz)
arbol = registro_nodos(raiz)
print(arbol)
buscar_nodo(arbol,5)
buscar_nodo(arbol, 7)

