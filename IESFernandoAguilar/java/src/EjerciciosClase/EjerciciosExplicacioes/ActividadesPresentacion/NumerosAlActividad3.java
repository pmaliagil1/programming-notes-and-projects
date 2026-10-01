package EjerciciosClase.EjerciciosExplicacioes.ActividadesPresentacion;

import java.util.Random;

public class NumerosAlActividad3 {
    public static void main(String[] args) {
        
        Random rd = new Random();

        final int CANTIDAD = 50;
        int maximo = 0;
        int minimo = 201;
        int suma = 0;
        for(int i = 0; i < CANTIDAD ; i++){
            int num = rd.nextInt(100)+100;
            suma = suma + num;
            if (maximo < num){
                maximo = num;
            }
            if (minimo > num){
                minimo = num;
            }

            System.out.print(num + " ");
        }
        System.out.println();
        System.out.println("La media es: " + (suma/CANTIDAD));
        System.out.println("El máximo es: "+ (maximo));
        System.out.println("El mínimo es: "+ (minimo));
    }
}
