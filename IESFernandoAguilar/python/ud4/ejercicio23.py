def suficiente(palabra, letra, cantidad):
    contador = 0
    
    for caracter in palabra:
        if caracter == letra:
            contador += 1
            
        if contador >= cantidad:
            return True
    

    return False


if __name__ == "__main__":

    print(suficiente('sisters', 's', 3))    
    print(suficiente('mississippi', 'i', 5))      
    print(suficiente('videoconference', 'e', 3))  
