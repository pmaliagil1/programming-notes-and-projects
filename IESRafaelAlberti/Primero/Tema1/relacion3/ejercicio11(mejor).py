#Hecho por victor, esta mejor que el mio
impares = 0
pares = 0
for i in range(100,201):
    if i%2 == 0:
        pares += i
    else:
        impares += i
print(f"Pares = {pares}\nImpares = {impares}")
