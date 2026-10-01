/*Un puntero se puede reutilizar para que apunte a otra variable pero esta debe ser del mimso tipo*/

#include <iostream>

int main(){
    float recurso_visual_en_los_simpsons = 1.61803;
    float numero_misterioso_en_doctor_who = 1.61803;

    float * numero_aureo = &recurso_visual_en_los_simpsons;
    std::cout <<numero_aureo<< std::endl; //std::endl sirve para el cambio de linea
    numero_aureo = &numero_misterioso_en_doctor_who;
    std::cout << numero_aureo<< std::endl;
}