"""Realiza un programa que compruebe la letra del DNI y detecte si el 
usuario se ha equivocado con los números."""

#Tuplas con las letras del DNI segun el modulo 23
letrasDni = (
    'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 
    'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'
)

#Pedios el DNI completo
dni = input("Introduce tu DNI completo (número y letras, sin espacios): ")
dni = dni.upper()

#Validamos que tenga al menos 2 caracteres
if len(dni) < 2 or not dni[:-1].isdigit() or not dni[-1].isalpha():
    print("Formato incorrecto. Debes introducir el número seguido de la letra")
else:
    try:
        numero = int(dni[:-1])
        letraUsuario = dni[-1]
        letraCorrecta = letrasDni[numero%23] #comrpueba que la letra sea la correcta, ya que la suma de los digitos del dni da la letra que te toca
    except ValueError:
        print("Fallo en la conversion")
    except IndexError:
        print("Has meado fuera de tiesto.")
    
    if letraUsuario == letraCorrecta:
        print("El DNI es correcto.")
    else:
        print(f"La letra es incorrecta. Deberia ser {letraCorrecta}")

