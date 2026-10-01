#Ejercicio 2: Ahora Saludo personalizado

def saluda2(nombre):
    print("Hola " + nombre)

if __name__=="__main__":
    nombre = input("Dime tu nombre: ") #Esta variable nombre no es la misma que la de la funcion
    saluda2(nombre)