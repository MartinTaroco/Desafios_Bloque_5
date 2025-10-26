#Desarrolla un programa que cree un archivo prestamos.txt y permita al usuario agregar el registro de un préstamo. El registro debe incluir el nombre del libro, el nombre del prestatario y la fecha del préstamo. Asegúrate de no sobrescribir el archivo cada vez que se agrega un nuevo préstamo.



def agregar(libro,usuario, fecha):
   with open(r"c:\Users\taroc\OneDrive\Escritorio\Profesorado de Informática\Desafios Bloque 5\prestamos. txt", "a") as archivo:
     archivo.write(f" {libro}, {usuario}, {fecha} \n")
     
     
agregar("Libro1", "Fulano1", "22/06/08")
agregar("Libro2", "Fulano2", "2/07/08")
agregar("Libro3", "Fulano3", "4/08/08")