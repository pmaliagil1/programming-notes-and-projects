num1 = int(input("Ingresa un primer número: "))
num2 = int(input("Ingresa un segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
if num1 % 2 != 0:
    num1 = num1 +1
print(f"Números pares entre los dos números: ")
while num1 <= num2:
    print (num1)
    num1 = num1 +2
