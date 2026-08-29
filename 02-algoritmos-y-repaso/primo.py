class PruebaPrimo:

    def es_primo(self, numero):
        try:
            num = int(numero)
            if num < 1:
                print("Número no natural o natural no mayor que 1")
                return False
            else:
                for i in range(2, num):
                    if num % i == 0:
                        return False
                return True
        except ValueError:
            print("Por favor, ingrese un número natural válido.")
            return False


if __name__ == "__main__":
    prueba = PruebaPrimo()

    n = input("Dime un número: ")

    print(f"{n} es primo: {prueba.es_primo(n)}")
