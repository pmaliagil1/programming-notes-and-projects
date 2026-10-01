def suma(lista1, lista2):

    max_len = max(len(lista1), len(lista2))
    
    resultado = []
    
    for i in range(max_len):
        valor1 = lista1[i] if i < len(lista1) else 0
        valor2 = lista2[i] if i < len(lista2) else 0
        
        resultado.append(valor1 + valor2)
    
    return resultado

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]

resultado = suma(lista1, lista2)
print("Lista resultante de la suma:", resultado)
