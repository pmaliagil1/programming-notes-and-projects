"""Dibuja un ordinograma de un programa que dada una cantidad de euros
que el usuario introduce por teclado (múltiplo de 5 €) mostrará los billetes de
cada tipo que serán necesarios para alcanzar dicha cantidad (utilizando
billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de
billetes posible. Por ejemplo, si el usuario introduce 145 el programa indicará
que será necesario 1 billete de 100 €, 2 billetes de 20 € y 1 billete de 5 € (no
será válido por ejemplo 29 billetes de 5, que aunque sume 145 € no es el
mínimo número de billetes posible)."""

def cuentaBilletes(n):
    billete500 = 0
    billete200 = 0
    billete100 = 0
    billete50 = 0
    billete20 = 0
    billete10 = 0
    billete5 = 0
    while n !=0:
        if n <0:
            raise ValueError("NO PUEDE SER NEGATIVO")
        if n >= 500:
            billete500 = n//500
            n = n%500
        if n>=200:
            billete200 = n//200
            n = n%200
        if n>=100:
            billete100 = n//100
            n = n%100
        if n>=50:
            billete50 = n//50
            n = n%50
        if n>=20:
            billete20 = n//20
            n = n%20
        if n>=10:
            billete10 = n//10
            n = n%10
        if n>=5:
            billete5 = n//5
            n = n%5
        
        return f"Billete 500:{billete500}\nBillete 200:{billete200}\nBillete 100: {billete100}\nBillete 50:{billete50}\nBillete 20:{billete20}\nBillete 10:{billete10}\nBillete 5:{billete5}"
        
        



if __name__ == "__main__":
    try:
        n = int(input("Introduce la cantidad de euros (multiplo de 5): "))
        if n%5 != 0:
            raise ValueError("NO ES MULTIPLO DE 5")
        print(cuentaBilletes(n))
    except ValueError:
        print("Debe ser multiplo de 5 y positivo")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
