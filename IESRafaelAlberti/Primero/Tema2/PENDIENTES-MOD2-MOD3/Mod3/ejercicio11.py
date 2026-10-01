"""Dibuja un ordinograma de un programa que suma independientemente los
pares y los impares de los números comprendidos entre 100 y 200, y luego
muestra por pantalla ambas sumas."""

#ESTA MAL ENTENDIDO, DEBAJO ESTÁ BIEN
def sumaParImpar():
    n = 0
    sumaPar = 0
    sumaImpar = 0
    while n != -1:
        try:
            n = int(input("Introduce un número entre 100 y 200 (-1 para terminar): "))
            if n <100 or n>200:
                raise ValueError ("DEBE SER ENTRE 100 Y 200")
            if n%2 == 0:
                sumaPar = sumaPar+n
            elif n %2 != 0:
                sumaImpar = sumaImpar+n
        except ValueError:
            print("Valor no válido")
        except Exception as e:
            print(f"Algo ha salido mal: {e}")
    return f"Suma par: {sumaPar}\nSuma impar: {sumaImpar}"

if __name__ == "__main__":
    print(sumaParImpar())

    #ES ASI:
    def ordinograma_par_imp():
        sumar_par = 0
        suma_impar = 0
        for i in range(100, 201):
            if i % 2 == 0:
                sumar_par += i
            else:
                suma_impar += i
        print(f"par: {sumar_par} impar_ {suma_impar}  ")

if __name__ == "__main__":
    try:
        ordinograma_par_imp()
    except Exception as e:
        print(f"Algo ha salido mal: {e}")