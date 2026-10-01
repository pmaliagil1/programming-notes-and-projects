/*Rescata el ejercicio 3.04. ¿Tu respuesta variaria en funcion del lenguaje (C / C++)?*/


int main(){
    float minuto = 4.73;
    return 0;
}


/* ¿Variaría entre C y C++? 
   Técnicamente NO: Ambos lenguajes aceptan 'float' para este valor.
   
   Diferencias sutiles:
   1. En C: Se suele usar el sufijo 'f' (4.73f) para evitar que el compilador 
      lo trate como 'double' y ahorrar un paso de conversión.
   2. En C++: Aunque 'float' funciona, la recomendación moderna es usar 'double' 
      por defecto para evitar errores de precisión, a menos que la memoria sea crítica.
   3. Impresión: C con printf() mostrará ceros extra (4.730000) por defecto, 
      mientras que C++ con cout es más "inteligente" y muestra solo 4.73.
*/