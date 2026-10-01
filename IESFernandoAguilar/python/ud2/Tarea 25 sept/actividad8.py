usuario = input("Introduzca el nombre de usuario: ")
contrasenia = int(input("Introduzca una contraseña: "))
match usuario:
    case "pepe":
      
        if contrasenia == 1234:
            print("Has entrado en el sistema")
        else:
            print ("Error.")
    
    case _:
        print("Error.")
