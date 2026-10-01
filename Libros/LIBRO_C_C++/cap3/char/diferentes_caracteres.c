/*Un char ocupa 8 bits en la memoria. Esto significa que puede tener $2^8 = 256$
combinaciones diferentes.Valores negativos y positivos: Por defecto, en la mayoría de sistemas es un
signed char, lo que significa que puede almacenar números del -128 al 127.Solo positivos: Si lo
usas como unsigned char, puede ir del 0 al 255.*/

//cualquier letra, numero o simbolo puede ser un char

int main(){
    char punto = ".";
    char arroba = "@";
    char cifra = "7";
    char espacio = " ";

    return 0;
}

//tambien se pueden declarar y definir variables en una sola linea

int main(){
    char punto = ".", arroba = "@", cifra = "7", espacio = " ";

    return 0;
}