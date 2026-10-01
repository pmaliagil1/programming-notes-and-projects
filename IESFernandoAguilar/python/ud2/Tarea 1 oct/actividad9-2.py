import math

N = int(input("Introduce un número: "))
es_primo = 1 
if N < 2:
    es_primo = 0
else:
    limite = int(math.sqrt(N)) + 1
    for i in range(2, limite):
        if N % i == 0:
            es_primo = 0  
            break
if es_primo == 1:
    print(f"{N} es primo.")
else:
    print(f"{N} no es primo.")
