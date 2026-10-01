/*Crea un puntero nulo en C, de tipo float*, y dotalo mas tarde de valor*/
#include <stdio.h>
int main(){
    float * punteroNulo = NULL;
    float variableReal;
    punteroNulo = &variableReal;
    *punteroNulo = 15;

    printf("%f", *punteroNulo);
    return 0;

}




/*
#include <stdio.h>
int main(){
    int *proveedor = NULL; //Con esto el puntero apunta a 0 (nada)
    printf("%p",proveedor);
    return 0;

}*/