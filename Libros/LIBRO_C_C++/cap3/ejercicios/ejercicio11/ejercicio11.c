/*Declara una variable de tipo float y asignale este valor:
1.7976931348623157e+308. Muestra su informacion en pantalla en C. ¿Que ocurre? Comprueba
si el valor mostrado en pantalla cambia si implementas el codigo en C++*/

#include <stdio.h>

int main(){
    float valor = 1.7976931348623157e+308;
    printf("Valor: %f",valor);
    return 0;

}

//Hay overflow de datos, si en vez de float usamos double funcionaria correctamente