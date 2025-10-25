#Construye un árbol binario en el que cada nodo contiene un número entero. Implementa una función que recorra el árbol en postorden y devuelva el valor máximo encontrado entre todos los nodos del árbol.

class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.izquierda = None
    self.derecha = None
    
nodos = []   
def pre_order(nodo):

 if nodo:
    print(nodo.valor, " ")
    nodos.append(nodo.valor)    #Despues de que verifica si existe el nodo, lo printea y lo agrega a la lista.
    pre_order(nodo.izquierda)
    pre_order(nodo.derecha)


raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)


pre_order(raiz)
print(max(nodos))    