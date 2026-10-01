"""Crear un programa que permita al usuario ingresar los montos de las compras de un 
cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada 
ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa 
un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al 
finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total 
de $1000, se le debe aplicar un 10% de descuento."""

def montoCliente():
    total = 0
    monto = -1
    while monto !=0:
        try:
            monto = int(input("Introduce la cantidad de dinero que desea cargar:"))
            if monto < 0:
                raise ValueError ("NO SE PUEDE INTRODUCIR DATOS NEGATIVOS")
            else:
                total+= monto
        except ValueError:
            print("Dato no válido")

    if total > 1000:
        print("Tu monto supera los 1000€, se le aplicará un 10% de descuento")
        total = total-(total*0.10)
        print(f"Su total a pagar es de: {total}€")
    else:
        print(f"Su total a pagar es de {total}")
        


if __name__ == "__main__":
    try:
        montoCliente()
    except Exception as e:
        print(f"Algo ha salido mal: {e}")