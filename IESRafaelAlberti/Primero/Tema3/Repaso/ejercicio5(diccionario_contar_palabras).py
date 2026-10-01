"""5. Diccionario: Contar palabras
Dado un texto, crea un diccionario donde las claves sean palabras y los valores el número de veces
que aparecen.
Pista: divide el texto en palabras con .split().
"""

def contarPalabras(texto_ejemplo):
    conteo = {}
    lista_texto = texto_ejemplo.split(" ")
    for palabra in lista_texto:
        if palabra in conteo:
            conteo[palabra]+=1
        else:
            conteo[palabra] = 1
    return conteo




if __name__ == "__main__":
    try:
        texto_ejemplo = "manzana pera manzana uva pera manzana platano uva"
        print(f"{contarPalabras(texto_ejemplo)}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")