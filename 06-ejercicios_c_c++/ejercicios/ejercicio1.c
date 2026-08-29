/*Declara un puntero a int que almacene la dirección de memoria de otra variable edad.
Inicializa edad a traves del puntero y muestra su informacion en
pantalla en C (tambien a traves del puntero)*/
#include <stdio.h>
int main(){
    int edad;
    int * punteroEdad = &edad;
    *punteroEdad = 15;
    printf("%d\n",edad);
    printf("%d",*punteroEdad);
    return 0;
}