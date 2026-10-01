"""2. Escritura en Archivo de Texto: Crea un programa que pida 3 frases al usuario y las
guarde, una por línea, en un archivo llamado notas.txt."""

frase1 = input("Introduzca una primera frase: ")
frase2 = input("Introduzca una segunda frase: ")
frase3 = input("Introduzca una tercera frase: ")

with open("notas.txt","w") as f:
    f.write(frase1 + "\n")
    f.write(frase2 + "\n")
    f.write(frase3)