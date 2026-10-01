
#include <iostream>

int main(){
    double numero_perdido = 48151.2342;
    double * p_numero_perdido = &numero_perdido;

    *p_numero_perdido = 15.16; //si cambio el valor al que apunta un puntero cambio el valor de la variable original

    std::cout<<numero_perdido<<std::endl;

    return 0;
}