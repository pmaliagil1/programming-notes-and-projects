pares = 0
impares = 0
for i in range (100,201,2):
    pares += i

for i in range (100,201):
    if i % 2 != 0:
        impares += i
    else:
        i = 0
print(f"Pares = {pares}\nImpares = {impares}")
