def maximo_comun_divisor(n1,n2):
    if n2 == 0:
        return n1
    return maximo_comun_divisor(n2,n1%n2)

if __name__=="__main__":
    n1=int(input())
    n2=int(input())
    resultado=maximo_comun_divisor(n1,n2)
    print(resultado)