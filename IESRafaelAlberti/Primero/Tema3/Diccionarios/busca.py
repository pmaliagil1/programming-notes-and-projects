def extraerEmail(cadena):
    if len(cadena)>0:
        posicion_arroba = cadena.find('@')
        if posicion_arroba==1:
            return None
        
        # Buscamos donde empieza el email recorriendo a izquierdas hasta
        inicio = posicion_arroba
        while inicio >0 and cadena[inicio]!=' ':
            inicio = inicio-1

        #Misma operacion recorriendo la cadena hasta encontrar otros espaci
        fin = posicion_arroba
        while fin<len(cadena)-1 and cadena[fin+1]!=' ':
            fin=fin+1

        #Lo devolvemos rebanado
        return cadena[inicio:fin]


nombre = input("Dime un email a ver si lo encuentro: ")
handler = open("mailbox.txt")
for linea in handler:
    palabras = linea.split()
    if len(palabras) > 0 and palabras[0] == "From:":
        email = extraerEmail(linea)
        if (nombre in linea):
            print(f"El dia de la semana es: {palabras[2]}")
            print(f"Email encontrado: {email}")
            