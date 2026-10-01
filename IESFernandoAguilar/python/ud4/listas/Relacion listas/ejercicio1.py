


#respuesta parte ejercicio 1 (no todo)

from random import sample

def gen_sin_repetir(n,inf,sup):
    lista_sin_repetir = list(range(inf,sup+1))
    return sample(lista_sin_repetir, k=n)

if __name__ == "__main__":
    n,inf,sup = 15,1,10
    print(gen_sin_repetir(n,inf,sup))