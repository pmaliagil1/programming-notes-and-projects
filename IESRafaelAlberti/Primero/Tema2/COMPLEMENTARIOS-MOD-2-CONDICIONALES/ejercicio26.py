#Diseñe un algoritmo que lea un número de tres cifras y determine si es capicúa.

def capicua(n):
    n = str(n)
    alreves = n[::-1]
    if alreves == n:
        return "Es capicúa"
    elif alreves != n:
        return "No es capicúa"

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número de tres cifras: "))
        if n <100 or n>999:
            raise ValueError("DEBE SER DE TRES CIFRAS")
        print(capicua(n))
    except ValueError:
        print("Debe ser un número de tres cifras")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")