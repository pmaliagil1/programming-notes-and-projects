"""Dado el conjunto de letras:
vocales = {'a', 'e', 'i', 'o', 'u'}
1. Crea un conjunto consonantes que contenga las letras del alfabeto que no son 
vocales.
2. Crea un conjunto letras_comunes que contenga las letras que están tanto en el 
conjunto vocales como en el conjunto consonantes.
3. Crea un subprograma que dado cualquier conjunto de este ejercicio sea capaz de 
escribirlo en la pantalla. (Si lo has creado antes, reutilízalo)"""
import string

def conjuntoLetras(vocales, alfabeto):
    alfabeto_set = set(alfabeto)
    consonantes = alfabeto_set - vocales
    letras_comunes = vocales.intersection(consonantes)
    return letras_comunes, consonantes

def mostrar(nombre, conjunto):
    print(f"Conjunto de {nombre}: {conjunto}")

if __name__ == "__main__":
    try:
        alfabeto_string = string.ascii_lowercase
        vocales = {'a', 'e', 'i', 'o', 'u'}
        letras_comunes,consonantes = conjuntoLetras(vocales, alfabeto_string)
        mostrar("Vocales", vocales)
        mostrar("Comunes", letras_comunes)
        mostrar("Consonantes", consonantes)    
    except Exception as e:
        print(f"Algo ha salido mal: {e}")