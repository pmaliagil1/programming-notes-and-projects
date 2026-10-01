import random

class AdivinaNumero:
    def __init__(self):
        self.numero_secreto = random.randint(1, 10)
        self.intentos = 5
    
    def jugar(self, max_intentos, entradas):
        for intento in range(max_intentos):
            if isinstance(entradas[intento], int):
                if entradas[intento] == self.numero_secreto:
                    return True
                elif entradas[intento] > self.numero_secreto:
                    print("El número secreto es menor.")
                else:
                    print("El número secreto es mayor.")
            else:
                print("Entrada no válida.")
                return False
        return False
