#Tienes dos listas de números enteros de diferentes longitudes. Desarrolla un programa que sume los elementos de las listas en las posiciones correspondientes. Si una lista es más corta que la otra, los elementos que falten deben considerarse como 0 en la suma.
lista_1 = [1, 2, 3, 4, 1,2,3,4,5,6]

lista_2 =[2,4,5,6,7,8,9,10]

lista_suma=[]

longitud_1 = len(lista_1)
longitud_2 = len(lista_2)


#Debajo comprobamos cual lista es mayor que la otra en cuanto a longitud, y le agregamos a la lista de menos longitud, una cantidad de ceros igual a esa diferencia
if longitud_1 > longitud_2:
  diferencia = longitud_1 - longitud_2
  while diferencia > 0:
    lista_2.append(0)
    diferencia -=1
    
else:
  diferencia =longitud_2 -longitud_1
  while diferencia > 0:
    lista_1.append(0)
    diferencia -=1
    
    
print(lista_1)
print(lista_2)

for i in range(0, len(lista_1)):
 suma = lista_1[i] + lista_2[i]
 lista_suma.append(suma) 
 
    
print(lista_suma)