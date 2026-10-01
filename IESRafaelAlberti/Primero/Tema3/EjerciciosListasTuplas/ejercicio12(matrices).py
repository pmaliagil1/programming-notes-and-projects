"""Escribir un programa que almacene las matrices 
matriz 2x3 
A= 
 1, 2, 3
 4, 5, 6
matriz 3x2 
B= 
−1, 0 
 0, 1
 1, 1
en una lista y muestre por pantalla su producto. El resultado debe ser una matriz de 2x2.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada 
vector fila en una lista.
Prueba ahora con estas matrices 
El resultado debe ser una matriz de 3x3"""

def dimensiones(m):
    """Funcion que calcula las dimensiones de una matriz. Devuelve numFilas x numColumnas"""
    if len(m)>0: 
        xm = len(m)
        ym = len(m[0])
        return xm,ym
    else:
        raise NameError("No es una matriz valida")
    
def multiplicable(a,b):
    """Funcion que devuelve Verdadero si se puede multiplicar por b"""
    x,y = dimensiones(a)
    z, t = dimensiones(b)

    if y==z:
        return True
    else:
        return False
    
def multiplicar(a,b):

    x,y=dimensiones(a)
    z,t=dimensiones(b)

    if multiplicable(a,b):
        #inicializar resultante
        resultante = []
        for p in range(0,x):
            fila = [0]*t
            resultante.append(fila)

        for i in range(0,x):
            for j in range(0,t):
                for k in range(0,y):
                    resultante[i][j]+=a[i][k]*b[k][j]

        return resultante
    else:
        raise NameError("MATRICES NO MULTIPLICABLES")
    
if __name__ == "__main__":
    a = [[1,2,3],[4,5,6]]
    b = [[-1,0],[0,1],[1,1]]
    try:
        print(multiplicar(a,b))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

