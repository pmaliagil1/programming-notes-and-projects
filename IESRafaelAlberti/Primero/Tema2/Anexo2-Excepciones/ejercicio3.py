#Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
# Deberá solicitar el número hasta introducir uno correcto.

num=-1
while (num != 0):
    try:
        num=int(input("Número: "))
    except ValueError:
        print("Valor incorrecto")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
    else:
        if num > 0:
            salida = ""
            for i in range(num,-1,-1):
                salida = salida + str(i)+","
            print(salida[:-1])
        else:
            print("Valor erróneo, sólo positivos porfavor")
    finally:
        print("Hasta luego")