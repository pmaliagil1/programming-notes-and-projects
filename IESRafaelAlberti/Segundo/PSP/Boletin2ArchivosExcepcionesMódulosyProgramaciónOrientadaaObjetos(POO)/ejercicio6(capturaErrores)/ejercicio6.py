"""6. Manejo de Excepciones Múl<ples: Crea una función dividir_elementos(lista,
indice, divisor) que intente acceder a un elemento de la lista por su índice y
dividirlo por el divisor. Captura y ges<ona específicamente IndexError y
ZeroDivisionError."""

def dividir_elementos(lista, indice, divisor):
    resultado = lista[indice]//divisor
    return resultado

if __name__ == "__main__":
    try:
        lista = [6,8,24,87,435,48,98,2345]
        indice = int(input("Introduce el indice: "))
        if indice <0 or indice > 7:
            raise IndexError
        divisor = int(input("Introduce el divisor: "))


        print(f"El resultado es: {dividir_elementos(lista, indice, divisor)}")
    except IndexError:
        print("Indice no válido")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")