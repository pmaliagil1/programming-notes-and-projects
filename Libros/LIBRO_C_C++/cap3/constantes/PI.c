/*el contenido de una variable puede cambiar a lo largo del programa, pero hay veces que usas
datos como el valor PI que son constantes, para eso se usa la palabra reservada const,
la cual es una variable que no permite ser cambiada tras su inicialización*/

int main(){
    const float PI = 3.14;
    //PI = 3.1415;   Esto no funcionaria ya que estamos tratando con un valor constante (saltaria error)
    return 0;
}

