#Tienes una tabla de calificaciones representada como una matriz, donde cada fila contiene las calificaciones de un estudiante en distintas materias. Implementa una función que busque una calificación específica en toda la matriz y devuelva el estudiante y la materia en la que se encuentra.


calificaciones =[
  [1, 2, 9],   #Indice 0
  [2, 10, 5],  #Indcie 1
  [3, 1, 9]   #Indice 2
  
]

#No logre asiganrle a cada fila de la matriz un estudiante, si bien si pude asignarle a cada columna una asignatura.

def buscar(calificaciones, nota):
  
  for estudiante, notas in enumerate(calificaciones):  #Accedo a cada (indice, fila)
   
    for materia, calificacion  in enumerate(notas):  #En cada interación de arriba, accedo a cada (materia, nota) donde materia seria la columna(indice de la fila, nota seria el valor)
        print(f"El estudiante numero {estudiante}", f"Sus notas {notas}")
        print(materia, calificacion)
        if calificacion == nota :
            if materia == 0:
              print(f"{estudiante} tiene esa nota en mate")
            if materia == 1:
              print(f"{estudiante} tiene esa nota en Biologia")
            if materia == 2:
              print(f"{estudiante} tiene esa nota en Física")
     
              
buscar(calificaciones, 9)