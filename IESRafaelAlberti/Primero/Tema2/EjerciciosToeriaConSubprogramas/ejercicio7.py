#Los tramos impositivos para la declaración de la renta en un determinado país son los
#siguientes:
#Renta Tipo impositivo
#Menos de 10000€ 5%
#Entre 10000€ y 20000€ 15%
#Entre 20000€ y 35000€ 20%
#Entre 35000€ y 60000€ 30%
#Más de 60000€ 45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
#tipo impositivo que le corresponde. 

def tipoRenta(b):
    resultado = 0
    if bruto<0:
        raise NameError("VALORES NEGATIVOS ES TRMAPA")
    else:
        if b<10000:
            resultado = 0.05        #Lo podemos ir haciendo poniendo return 0.05
        elif b<20000:
            resultado = 0.15        #return 0.15
        elif b<35000:
            resultado = 0.20        #return 0.20
        elif b<60000:
            resultado = 0.30        #return 0.30
        else:
            resultado = 0.45        #return 0.45

        return resultado            #En caso de hacer todo con return este retun no hay que hacerlo
    

if __name__ == "__main__":
    try:
        bruto = float(input("Dime tu salario bruto anual: "))
        tipo = tipoRenta(bruto)
        print(f"Te corresponde pagar: {bruto*tipo}")
        print(f"El salario neto quedaría: {bruto-bruto*tipo}")

    except ValueError:
        print("Datos de entrada erróneos")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")