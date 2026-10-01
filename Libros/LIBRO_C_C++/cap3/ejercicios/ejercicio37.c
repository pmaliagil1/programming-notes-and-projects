/*¿Que ocurre si asignas un valor de tipo float a una variable entera?
Muestra su contenido en pantalla y estudia su comportamiento*/

#include <stdio.h>

int main(){
    int variable = 10.65; // El valor real almacenado será 10
    printf("Valor: %d", variable);
    return 0;
}

/* ¿Qué ocurre al asignar un float a un int? 
   Ocurre una conversión implícita por TRUNCAMIENTO. El compilador 
   elimina la parte decimal (no redondea) y solo almacena la parte 
   entera. Se considera una "conversión con pérdida" de información. */