A,B,C = input ("Ingresa tres valores: ").split()
print ("Usted ha seleccionado para A: ",A," para B: ",B, "y para C: ",C,)
aux = A
A = B
B = C
C = aux
print ("Intercambiando valores.")
print ("Los valores han sido intercambiados.")
print ("A: ",A)
print ("B: ",B)
print ("c: ",C)
