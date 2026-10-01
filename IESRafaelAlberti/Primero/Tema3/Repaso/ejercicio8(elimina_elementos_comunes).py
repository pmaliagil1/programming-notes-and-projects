"""8. Conjuntos: Eliminar elementos comunes
Dado un conjunto A y un conjunto B, elimina del conjunto A todos los elementos que estén en B.
Pista: se pueden usar métodos como difference_update() u operadores como -=."""

def eliminaElementosComunes(conjunto_a, conjunto_b):
    conjunto_a -= conjunto_b
    return conjunto_a

if __name__ == "__main__":
    try:
        conjunto_a = {1, 2, 3, 4, 5}
        conjunto_b = {4, 5, 6, 7}
        print(eliminaElementosComunes(conjunto_a, conjunto_b))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")