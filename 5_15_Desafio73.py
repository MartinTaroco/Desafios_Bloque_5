#Tienes una lista de números en la que algunos elementos están repetidos. Desarrolla un programa que elimine todos los elementos duplicados y deje únicamente una aparición de cada uno. La salida debe mostrar la lista original y la lista sin duplicados.


lista = [1,1,2, 4, 4, 4, 5]

lista_sin_duplicados = []


for i in lista:
  if i not in lista_sin_duplicados:
    lista_sin_duplicados.append(i)
    
    

print(lista)   
print(lista_sin_duplicados)