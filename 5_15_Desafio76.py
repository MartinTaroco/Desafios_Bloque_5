#Construye un árbol binario simple con al menos 3 niveles de profundidad. Cada nodo debe contener un número entero como valor. Una vez construido el árbol, implementa una función que imprima los valores de los nodos siguiendo un recorrido en preorden.

class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.izquierda = None
    self.derecha = None
    
    
def pre_order(nodo):
 if nodo:
    print(nodo.valor, " ")
    pre_order(nodo.izquierda)
    pre_order(nodo.derecha)


raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)


pre_order(raiz)    