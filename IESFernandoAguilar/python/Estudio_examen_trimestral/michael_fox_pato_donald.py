def verificar_cumpleanios_repetidos():
    n = int(input())

    while n != 0:
        fechas = input().split()

        cumpleanios = []

        for fecha in fechas:
            if fecha in fechas:
                print("SI")
                break 
        else:
            print("NO")

        n = int(input())

if __name__ == "__main__":
    verificar_cumpleanios_repetidos()
