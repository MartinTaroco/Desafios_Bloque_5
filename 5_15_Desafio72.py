#Un sistema de inventario tiene una lista con los códigos de productos. Desarrolla un programa que permita al usuario introducir un código de producto y que determine si ese código está en la lista. Si el código se encuentra, el programa debe devolver la posición en la que aparece; si no está, debe mostrar un mensaje indicando que no se ha encontrado el código.


inventario = [234, 4567, 32, 5, 47]

def lector_de_codigo(codigo):
  if codigo in inventario:
    print("El producto se encuentra en la posición número: ", inventario.index(codigo))
  else:
    print("No contamos con ese producto")
    
    
  

lector_de_codigo(234)
lector_de_codigo(1)