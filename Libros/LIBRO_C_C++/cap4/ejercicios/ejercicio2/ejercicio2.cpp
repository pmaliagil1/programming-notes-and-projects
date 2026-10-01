/*Declara un puntero a entero que tome la direccion de memoria del valor 42 (&42).
¿Que crees que ocurre? Muestra el contenido del puntero en pantalla en C y C++*/
#include <iostream>
int main(){
    int valor = 42;
    int * punteroValor = &valor;
    std::cout<<"Valor del puntero: "<<*punteroValor<<std::endl;
    std::cout<<"Direccion del puntero: "<<punteroValor;

    return 0;

}