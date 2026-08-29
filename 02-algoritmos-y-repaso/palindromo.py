def palindromo(cadena):
    if len(cadena)==1:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return palindromo(cadena[1:-1])

if __name__=="__main__":
    cadena = input()
    print(palindromo(cadena))