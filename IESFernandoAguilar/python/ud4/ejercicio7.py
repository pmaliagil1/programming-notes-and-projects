def palabras_frase(frase):
    palabras = frase.split()
    return len(palabras)

frase = input("Introduce una frase: ")
num_palabras = palabras_frase(frase)
print(f"La frase tiene {num_palabras} palabras.")
