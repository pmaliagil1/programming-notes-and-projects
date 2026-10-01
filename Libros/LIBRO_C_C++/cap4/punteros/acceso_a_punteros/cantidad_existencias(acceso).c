#include <stdio.h>
int main(){
    int cantidad_existencias = 2342;
    int * proveedor1 = &cantidad_existencias;
    int * proveedor2 = &cantidad_existencias;
    int * proveedor3 = &cantidad_existencias;

    int numero_de_existencias = *proveedor1;/*De esta forma numero_de_existencias obtendra una copia del
    valor contenido en cantidad_existencias*/

    printf("Contenido de la cantidad de existencias: %d\n",numero_de_existencias);
    printf("Contenido de la cantidad de existencias desde proveedor1: %d",*proveedor1);//puede hacerse directamente
    return 0;
}