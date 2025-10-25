#Dado un árbol binario con números enteros en cada nodo, implementa una función que recorra el árbol en inorden y calcule la suma de todos los valores almacenados en los nodos. El programa debe devolver el resultado final de la suma.

class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.izquierda = None
    self.derecha = None
    


suma = 0  
def in_order(nodo):
  global suma     #Tengo que aclarar que voy a usar una variable antes declarada
  if nodo:
    suma = suma + nodo.valor
    in_order(nodo.izquierda)
    print(nodo.valor, " ")
    in_order(nodo.derecha)
  

raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)


in_order(raiz)    
print(suma)