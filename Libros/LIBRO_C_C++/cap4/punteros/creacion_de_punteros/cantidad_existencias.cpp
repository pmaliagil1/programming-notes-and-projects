/*Imagina que varios proveedores quieren acceder a la cantidad de existencias, cada uno tiene un puntero
que apunta a la misma direccion de memoria*/

#include <iostream>
int main(){
    int cantidad_existencias = 2342;
    int * proveedor1 = &cantidad_existencias; //escribe el tipo de valor al que apunta,*, y el nombre del puntero
    //para definir el puntero utilizamos & para tomar la direccion de memoria de cantidad_existencias
    std::cout<<proveedor1;
    return 0;
}