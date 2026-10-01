#pizzeria (copiar enunciado de moodle)

def eligeVegetariana():
    opcion = 0
    print("1.Vegetariana")
    print("2.Carne y/o Pescado")

    opcion = int(input("Opcion: "))
    match opcion:
        case 1:
            return True
        case 2:
            return False
        case _:
            raise NameError("OPCIÓN NO VÁLIDA")

def pintaMenuVegetariana():
    print("1.Pimiento")
    print("2.Tofu")

def pintaMenuCarnePescado():
    print("1.Pepperoni")
    print("2.Salmón")
    print("3.Jamón")

if __name__ == "__main__":
    try:
        ingredientesBase = "Tomate, Mozarella, "
        ingredienteEspecial = ""
        vegetariana = eligeVegetariana()
        if vegetariana:
            pintaMenuVegetariana()
            opcion = int(input("Opción: "))
            match opcion:
                case 1:
                    ingredienteEspecial = "Pimiento"
                case 2:
                    ingredienteEspecial = "Tofu"
                case _:
                    raise NameError("OPCIÓN NO VÁLIDA")
        else:
            pintaMenuCarnePescado()
            opcion = int(input("Opción: "))
            match opcion:
                case 1:
                    ingredienteEspecial = "Pepperoni"
                case 2:
                    ingredienteEspecial = "Salmón"
                case 3:
                    ingredienteEspecial = "Jamón"
                case _:
                    raise NameError("OPCIÓN NO VÁLIDA")
            
        print(f"Tu pizza tiene: {ingredientesBase}{ingredienteEspecial}")
    except ValueError:
        print("Error, el valor debe ser válido")
    except NameError as e:
        print(f"Opción no válida: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")
