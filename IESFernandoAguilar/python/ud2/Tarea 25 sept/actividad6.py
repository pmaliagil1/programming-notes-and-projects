num1 = int(input("Ingrese un primer número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))
num4 = int(input("Ingrese un cuarto número: "))
num5 = int(input("Ingrese un quinto número: "))
media = (num1 + num2 + num3 + num4 + num5) / 5
print(f"La media aritmétrica de los números seleccionados es {(media)}")
if num1 > media:
    print (f"{num1} es mayor que la media ({media})")    
if num2 > media:
    print (f"{num2} es mayor que la media ({media})")
if num3 > media:
    print (f"{num3} es mayor que la media ({media})")
if num4 > media:
    print (f"{num4} es mayor que la media ({media})")
if num5 > media:
    print (f"{num5} es mayor que la media ({media})")


