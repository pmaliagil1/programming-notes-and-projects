"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las 
facturas se almacenarán en un diccionario donde la clave de cada factura será el número 
de factura y el valor el coste de la factura. El programa debe preguntar al usuario si 
quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una 
nueva factura se preguntará por el número de factura y su coste y se añadirá al 
diccionario. Si se desea pagar una factura se preguntará por el número de factura y se 
eliminará del diccionario. Después de cada operación el programa debe mostrar por 
pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

def gestionarFacturas(facturas):
    cobrado = 0
    acabado = False
    
    while not acabado:
        print("\n--- MENU FACTURAS ---")
        accion = input("¿Quieres añadir, pagar o terminar?: ").lower()
        
        if accion == "terminar":
            acabado = True
        
        elif accion == "añadir":
            try:
                numero = input("Introduce el número de factura: ")
                coste = float(input("Introduce el coste: "))
                facturas[numero] = coste
            except ValueError:
                print("Error: El coste debe ser un número")
        
        elif accion == "pagar":
            numero = input("Introduce el número de factura a pagar: ")
            if numero in facturas:
                # Sacamos el valor y lo sumamos a lo cobrado
                valor = facturas.pop(numero)
                cobrado += valor
            else:
                print("Esa factura no existe")
        
        else:
            print("Opción no válida")

        # Calculamos lo que queda en el diccionario
        pendiente = sum(facturas.values())
        print(f"Cobrado hasta el momento: {cobrado}")
        print(f"Pendiente de cobro: {pendiente}")

if __name__ == "__main__":
    try:
        facturas_empresa = {}
        gestionarFacturas(facturas_empresa)
    except Exception as e:
        print(f"Algo ha salido mal: {e}")