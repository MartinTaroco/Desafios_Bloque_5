#Desarrolla un programa que, dado un conjunto de tres números enteros introducidos por el usuario, determine cuál de ellos es el mayor. Considera la posibilidad de que algunos o todos los números sean iguales. El programa debe imprimir un mensaje claro con el número mayor o indicar si todos los números son iguales.


i = 3
lista_de_numeros = []
while i>0:                             #Pedimos los tres números 
  numero = int(input("Dame un número entero: "))
  lista_de_numeros.append(numero)
  i -= 1 
  
lista_de_numeros.sort()   #Ordenamos la lista de menor amyor


posible_mayor = lista_de_numeros[2]               #Tomamos el ultimo elemento de la lista, posiblemente el mayor
if lista_de_numeros.count(posible_mayor) == 3:       #Verificamos si son todos iguales (El mayor se repite tres veces)
  print("los tres son iguales")
else: 
  print("El  mayor es", posible_mayor)