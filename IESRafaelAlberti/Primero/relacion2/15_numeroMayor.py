n1 = int(input("Introduce un primer numero: "))
n2 = int(input("Introduce un segundo numero: "))
n3 = int(input("Introduce un tercer numero: "))
if n1 >n2 and n1 > n3:
    print(f"El mayor es {n1}")
elif n2 > n1 and n2 > n3:
    print(f"El mayor es {n2}")
else:
    print(f"El mayor es {n3}")
