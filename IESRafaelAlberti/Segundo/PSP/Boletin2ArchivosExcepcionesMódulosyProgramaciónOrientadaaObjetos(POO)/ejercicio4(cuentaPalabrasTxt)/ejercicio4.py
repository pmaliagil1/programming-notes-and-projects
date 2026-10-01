"""4. Lector de Archivos con Conteo: Escribe un script que lea el archivo notas.txt
creado previamente y muestre por pantalla cuántas palabras totales con<ene el
archivo."""

file = open("../prog/notas.txt","r")
lista_aux = file.read()
palabras = lista_aux.split()
print(len(palabras))