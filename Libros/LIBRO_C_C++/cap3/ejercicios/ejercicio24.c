/*Muestra el contenido de un booleano en pantalla. ¿Que especificador de formato utilizarias?
¿Por que?*/

#include <stdbool.h>
#include <stdio.h>

int main(){
    bool variable = true;
    printf("Bool: %d",variable);
    return 0;
}
//Utilizo el formato de int ya que los valores de bool pueden ser 0 o 1