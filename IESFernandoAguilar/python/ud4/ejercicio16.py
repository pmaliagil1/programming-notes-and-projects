def dominio_ies(email):
    nombre_usuario = email.split("@")[0]
    nuevo_email = f"{nombre_usuario}@fernandoaguilar.es"
    return nuevo_email

if __name__ == "__main__":
    email = input("Ingresa tu correo electrónico: ")

    print("Correo con dominio 'fernandoaguilar.es':", dominio_ies(email))
