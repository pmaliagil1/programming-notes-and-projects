"""Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
(en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea 
uno o más."""

def cuentaPalabra(frase):
    contador = -1
    numeroGanador=0                 #ATENTO AL SPLIT AL ESTUDIAR
    almacenador = frase.split() #Aqui habias puesto split(" ") eso está mal ya que si hay mas de un espacio lo separa mal
    ganador = ""                
    for i in range(len(almacenador)):
        contador += 1
        if len(almacenador[i]) > len(ganador):
            ganador = almacenador[i]
            numeroGanador = contador

    print(f"La palabra más larga es '{ganador}', que esta en la posicion '{numeroGanador}'")
        
        

if __name__ == "__main__":
    try:
        frase = input("Introduzca una frase: ")
        cuentaPalabra(frase)
    except TypeError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")