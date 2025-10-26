

#Primero aclarar que se pueden usasr comparativos lógicos con string porque compara la primera letra

ana ="Ana"
belen = "Belen"

prueba = ana > belen

print(prueba)


#Dado lo anterior, la estructura es igual a que si se tratara de una lista con números
def buscar_estudiante(estudiantes, nombre):

    inicio = 0
    fin = len(estudiantes) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if estudiantes[medio].lower() == nombre.lower():
            return f"El estudiante '{nombre}' se encuentra en la posición {medio}."
        elif nombre.lower() < estudiantes[medio].lower():
            fin = medio - 1
        else:
            inicio = medio + 1

    return f" El estudiante '{nombre}' no se encuentra en la lista."
