#Tienes una lista de estudiantes y su promedio de calificaciones. Implementa un algoritmo que ordene a los estudiantes de acuerdo con su promedio utilizando el algoritmo de ordenamiento por selección. Al final, el estudiante con el promedio más alto debe estar en primer lugar.


# Lista de promedios
promedios = [10, 8, 11, 4, 12]

# Ordenamiento por inserción, tan solo cambie el comparador lógico por un mayor, para obtener un orden de mayor a menor.
def ordenamiento_insercion(promedios):
    for i in range(1, len(promedios)):
        clave = promedios[i]
        j = i - 1
        while j >= 0 and clave > promedios[j]:
            promedios[j + 1] = promedios[j]
            j -= 1
        promedios[j + 1] = clave


ordenamiento_insercion(promedios)
print(f"Los promedios son: {promedios}")
