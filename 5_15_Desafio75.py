#Usa una "list comprehension" para crear una lista llamada potencias que contenga las potencias de 2 de los números del 0 al 9 (es decir, 2 elevado a la potencia de cada número). Imprime la lista resultante.


lista= [2**i for i in range (0, 9)]


print(lista)