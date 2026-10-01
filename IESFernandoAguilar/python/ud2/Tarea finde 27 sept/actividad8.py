base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))
resultado = 1
contador = 0
while contador < exponente: 
    resultado = resultado * base
    contador = contador + 1 
print (f"{base} elevado a {exponente} es: {resultado}")