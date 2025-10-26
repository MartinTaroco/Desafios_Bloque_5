#Dado un archivo libros.txt que contiene una lista de libros y sus autores, implementa una función que busque todos los libros escritos por un autor específico y los muestre. Si el autor no tiene libros en la lista, debe mostrar un mensaje indicando que no hay coincidencias.

def buscar_libros(autor):
 esta = False   #USamso este marcador inciialm3ente en falso, para mas adelante
 with open(r"c:\Users\taroc\OneDrive\Escritorio\Profesorado de Informática\Desafios Bloque 5\prestamos. txt", "r") as archivo:
   for linea in archivo:
     if autor in linea:
       print("El autor esta en ", linea)  
       esta = True   #Si lo encuentra, cambia a true y no llama al if de abajo
   if not esta:   #Si no cambio a true, es porque no encontro, y llama al print
      
      print("No coincidencia")
            
buscar_libros("Fulano5")