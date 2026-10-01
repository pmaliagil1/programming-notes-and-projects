"""Escribir un programa que cree un diccionario de traducción español-inglés. El usuario 
introducirá las palabras en español e inglés separadas por dos puntos, y cada par 
<palabra>:<traducción> separados por comas. El programa debe crear un 
diccionario con las palabras y sus traducciones. Después pedirá una frase en español y 
utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el 
diccionario debe dejarla sin traducir"""

def diccionarioTraductor(diccionario):
    entrada = input("Introduce palabras (esp:ing, esp:ing): ")
    
    pares = entrada.split(",") 
    
    for par in pares:
        if ":" in par:
            esp, ing = par.split(":", 1)
            diccionario[esp.strip().lower()] = ing.strip()

    frase = input("Introduce una frase en español: ")
    
    palabras_frase = frase.lower().split()
    
    resultado = [diccionario.get(palabra, palabra) for palabra in palabras_frase]
    """Sin usar .get() (usando un bucle normal):

Python
if "mundo" in diccionario:
    traduccion = diccionario["mundo"]
else:
    traduccion = "mundo" # Tienes que escribir "mundo" a mano
Con .get():

Python
traduccion = diccionario.get("mundo", "mundo")
# Como "mundo" no existe, te devuelve el segundo "mundo" automáticamente."""
    print("\nTraducción:")
    print(" ".join(resultado))


if __name__ == "__main__":
    try:
        diccionario = {}
        diccionarioTraductor(diccionario)
    except Exception as e:
        print(f"Algo ha salido mal: {e}")