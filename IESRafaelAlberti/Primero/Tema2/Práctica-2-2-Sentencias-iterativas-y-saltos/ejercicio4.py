#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def cuentaAtras(n):
    resultado = ""
    for i in range(n,-1,-1):
        resultado = resultado+","+str(i)
    print(resultado[1:])
if __name__ == "__main__": 
    try:
        n = int(input("Introduce un número: "))
        cuentaAtras(n)

    except Exception as e:
        print(f"Error desconocido{e}")
    except ValueError:
        print("Valor no válido")