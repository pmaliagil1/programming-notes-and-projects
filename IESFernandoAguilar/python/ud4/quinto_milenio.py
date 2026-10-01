def buscar_mensaje(titular, mensaje):
    titular_normalizado = titular.lower()
    mensaje_normalizado = mensaje.lower().replace(" ", "")
    
    index_titular = 0
    index_mensaje = 0
    len_titular = len(titular_normalizado)
    len_mensaje = len(mensaje_normalizado)

    while index_titular < len_titular and index_mensaje < len_mensaje:
        if mensaje_normalizado[index_mensaje] == titular_normalizado[index_titular]:
            index_mensaje += 1 
        index_titular += 1

    return index_mensaje == len_mensaje

n = int(input())
resultados = []

for _ in range(n):
    titular = input().strip()
    mensaje = input().strip()
    if buscar_mensaje(titular, mensaje):
        resultados.append("SI")
    else:
        resultados.append("NO")

for resultado in resultados:
    print(resultado)
