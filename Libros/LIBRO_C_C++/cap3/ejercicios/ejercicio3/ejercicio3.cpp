/*Define una constante que almacene el valor del número e en ambos lenguajes (e = 2.71828)*/

int main(){
    const double e = 2.71828;
    return 0;
}

/*En C: Una variable const tiene enlace externo por defecto. Esto significa que el compilador la
trata como una variable normal a la que simplemente "le prohíben" cambiar.
Ocupa un lugar en la memoria RAM obligatoriamente.
En C++: Una variable const tiene enlace interno por defecto. C++ es más agresivo optimizando;
si ve que usas e, a veces ni siquiera le asigna una dirección de memoria, sino que "pega"
el número directamente en el código de la CPU (similar a un #define pero más seguro).*/