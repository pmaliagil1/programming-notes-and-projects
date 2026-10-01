/*Sustituye el especificador de formato que utilizaste en el ejercicio 3.05 por este
otro: %2.f. ¿Que ha ocurrido?*/

#include <stdio.h>

int main(){
    float explosivo = 3.6;
    printf("Explosivo: %2.f",explosivo);
    return 0;
}

//Se ha redondeado a 4