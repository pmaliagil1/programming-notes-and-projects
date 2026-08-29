def calcular_factorial(num):
    resultado = 1
    for i in range(2,num+1):
        resultado *= i
    return resultado

num_casos = int(input())
resultado = []

for _ in range(num_casos):
    num = (int(input()))
    resultado.append(calcular_factorial(num))

for res in resultado:
    print (res)