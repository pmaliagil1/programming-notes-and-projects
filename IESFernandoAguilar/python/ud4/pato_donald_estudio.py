def procesar_cumpleaños(numero_cumpleaños, fechas):
    for i in range(numero_cumpleaños):
        for j in range(i + 1, numero_cumpleaños):
            if fechas[i] == fechas[j]:
                return "SI"
    return "NO"

def main():
    while True:
        numero_cumpleaños = int(input())
        
        if numero_cumpleaños == 0:
            break
        
        fechas = input().split()
        
        resultado = procesar_cumpleaños(numero_cumpleaños, fechas)
        print(resultado)

if __name__ == "__main__":
    main()
