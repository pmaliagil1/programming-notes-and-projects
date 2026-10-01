package EjerciciosClase.EjerciciosExplicacioes.ActividadesPresentacion;


import java.lang.Math;
public class TresNumerosAleatoriosActividad6 {

        public static void main(String[] args) {
    
            final int CANTIDAD = 3;
            int maximo = -1;
            for(int i = 0; i < CANTIDAD ; i++){
                int num = (int) (Math.random() * 100)+1;
                if (maximo < num){
                    maximo = num;
                }
    
                System.out.print(num + " ");
            }
            System.out.println();
            System.out.println("El máximo es: "+ (maximo));
        }
    }
    