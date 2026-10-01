"""11. Ficheros
Procesar un fichero de texto usando listas
Dado un fichero de texto llamado datos.txt que contiene varias líneas con palabras separadas 
por espacios, se pide:
1. Leer el fichero y almacenar todas las palabras en una lista. 
2. Mostrar cuántas palabras hay en total. 
3. Crear una lista con las palabras únicas (sin repetir). 
4. Ordenar alfabéticamente la lista de palabras únicas. 
5. Mostrar los resultados. 
Contenido de ejemplo del fichero  datos.txt 
hola mundo esto es un ejemplo de fichero
python es un lenguaje poderoso y divertido
hola mundo python de ejemplo
Pista: Puedes utilizar otra estructura de datos auxiliar diferente a listas para realizar algún apartado. 
También te puedes inspirar en el ejercicio de clase sobre apertura y recorrido de ficheros"""
def pintaLista(l):
    for p in l:
        print(p)

#1. Leer el fichero y almacenar todas las paabras en una lista
f = open("datos.txt", "r")
palabras = []

for linea in f:
    palabras.extend(linea.split())

# 2. Mostrar cuantas palabras hay en total
print("Total de palabras: ", len(palabras))

# 3. Crear una lista con palabras unicas (sin repetir)
print("Las palabras unicas son las siguientes: ")
palabras_unicas = list(set(palabras))
pintaLista(palabras_unicas)

#4. Ordenar alfabeticamente la lista de palabras unicas
palabras_unicas.sort()

#5. Mostrar resultados
print("La lista con las palabras unicas ordenadas es la siguiente: ")
pintaLista(palabras_unicas)


