""" Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la
entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años
debe pagar 5€ y si es mayor de 18 años, 10€. 
 """

def dimePrecio(edad):
    if edad <0 or edad >150:
        raise NameError("La edad no es humana")
    else:
        if edad<4:
            return 0
        elif edad<18:
            return 5
        else:
            return 10
        
if __name__=="__main__":
    try:
        e = int(input("Dime tu edad: "))
        precio = dimePrecio(e)
        print(f"Tienes que pagar: {precio}")
    except ValueError:
        print("Valor de la edad no es válido")