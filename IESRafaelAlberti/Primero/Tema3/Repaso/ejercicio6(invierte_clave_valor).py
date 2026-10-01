"""6. Diccionario: Invertir claves y valores
Dado un diccionario simple (sin valores repetidos), crea otro donde las claves sean los valores y los
valores las claves.
Pista: Busca el ejercicio de clase donde se traduce de español a inglés y haz que funcione al revés."""

def invierteClaveValor(colores):
    invertido = {}
    for clave, valor in colores.items():  #Muy importante aprender a hacer esto.
        invertido[valor] = clave
    return invertido

if __name__ == "__main__":
    try:
        colores = {"rojo": "red", "verde": "green", "azul": "blue"}
        print(f"Diccionario original: {colores}\nDiccionario invertido: {invierteClaveValor(colores)}")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")