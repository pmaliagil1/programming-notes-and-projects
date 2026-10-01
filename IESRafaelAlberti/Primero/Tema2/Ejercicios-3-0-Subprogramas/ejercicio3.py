#Ejercicio 3: Multiplicar sin usar el símbolo * (dos números)

def multiplica(num1,num2):
    result = 0
    for i in range(num2):
        result = result + num1
    return (result)


if __name__ == "__main__":
    resultado = multiplica(2,5)
    print(resultado)