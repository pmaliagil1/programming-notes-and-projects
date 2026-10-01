numero = int(input("Ingrese un número de dos cifras: "))
decenas = numero // 10 
unidades = numero % 10
numero_invertido = (unidades * 10) + decenas
if numero > 99 or numero < 10:
    print ("El número debe de ser de dos cifras.")
else: print ("El número intercambiado es: ",numero_invertido)
     
    
