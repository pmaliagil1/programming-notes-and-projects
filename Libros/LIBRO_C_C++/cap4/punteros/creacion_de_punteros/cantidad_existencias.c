/*Imagina que varios proveedores quieren acceder a la cantidad de existencias, cada uno tiene un puntero
que apunta a la misma direccion de memoria*/

//PARA PONER VARIOS PUNTEROS DIFERENTES:
//los punteros proveedor1,proveedor2 y proveedor3 almacenaran el mismo contenido (cantidad_existencias)
#include <stdio.h>
int main(){
    int cantidad_existencias = 2342;
    int * proveedor1 = &cantidad_existencias;
    int * proveedor2 = &cantidad_existencias;
    int * proveedor3 = &cantidad_existencias;
    //para definir el puntero utilizamos & para tomar la direccion de memoria de cantidad_existencias
    printf("%p\n",proveedor1);
    printf("%p\n",proveedor2);
    printf("%p\n",proveedor3);

    return 0;
}