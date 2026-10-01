/*El numero aureo aparece tanto en los simpsons como en doctor who*/
#include <stdio.h>
int main(){
    float recurso_visual_en_los_simpsons = 1.61803;
    float * puntero_a_recurso_visual = &recurso_visual_en_los_simpsons;
    float numero_misterioso_en_doctor_who = 1.61803;
    float*puntero_a_numero_misterioso = &numero_misterioso_en_doctor_who;

    printf("%p\n",puntero_a_recurso_visual);
    printf("%p\n",puntero_a_numero_misterioso);


    return 0;
}