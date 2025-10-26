#Dado un árbol que representa los grupos de estudiantes en una escuela, implementa un recorrido por niveles para mostrar los estudiantes de cada grupo, comenzando por el nivel más alto (ej. grado 12) y descendiendo hasta el nivel más bajo (ej. grado 1). Cada nodo del árbol representa un grado y sus estudiantes.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def preorden(raiz):
    if raiz:
        print(raiz.valor)
        preorden(raiz.izq)
        preorden(raiz.der)


raiz = Nodo(10)
raiz.izq = Nodo(5)
raiz.der = Nodo(15)

preorden(raiz)
