def euros_centimos(precio):
    partes = precio.split(".")
    
    if len(partes) == 2 and len(partes[1]) == 2:
        euros = int(partes[0])
        centimos = int(partes[1])
        return euros, centimos
    return ()

if __name__ == "__main__":
    precio = input("Ingresa el precio del producto en euros (ejemplo: 19.99): ")

    resultado = euros_centimos(precio)

    if resultado:
        euros, centimos = resultado
        print(f"Euros: {euros}")
        print(f"Céntimos: {centimos}")
    else:
        print("Error: Ingresa el precio en el formato correcto, con dos decimales (por ejemplo, 19.99).")
