/*imagina que estas trabajando en una empresa que publica articulos, si tu articulo el primer dia
es visitado por mas de tres mil millones de personas, el redactor accede a ciertas campañas,
int solo puede recoger numeros que van desde -2 148 483 hasta 2 1483 647, por lo que el contador
nunca llegaria  mas de tres mil millones, usando unsigned eliminamos la posibilidad de representar
valores negativos, por lo que el rango positivo llega hasta n4 294 967 295 (un entero de 32 bits)*/

//sin unsigned
int main(){
    int visitas_primer_dia = 95720;
    return 0;
}

//con unsigned
int main(){
    unsigned int visitas_primer_dia = 3000000000; //si quitamos el int, el compilador entiende que te refieres a un entero
    return 0;
}