numero = int(input())

for i in range(numero):
    grupo = input()

    miembros = []
    partes = grupo.split(", ")
    
    for parte in partes:
        if " i " in parte:
            miembros += parte.split(" i ")
        else:
            miembros += [parte]

    iniciales = ""
    for miembro in miembros:
        miembro = miembro.strip()
        inicial = miembro[0].upper()

        if inicial == "Á":
            inicial = "A"
        elif inicial == "É":
            inicial = "E"
        elif inicial == "Í":
            inicial = "I"
        elif inicial == "Ó":
            inicial = "O"
        elif inicial == "Ú":
            inicial = "U"

        iniciales += inicial
    print(iniciales)
