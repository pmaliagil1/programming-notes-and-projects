package EjerciciosClase.EjerciciosExplicacioes;

import java.util.Scanner;

public class ProductoEscalar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] vector1 = new int[3];
        int[] vector2 = new int[3];

        System.out.println("Introduce los valores para el primer vector:");
        for (int i = 0; i < 3; i++) {
            vector1[i] = sc.nextInt();
        }

        System.out.println("Introduce los valores para el segundo vector:");
        for (int i = 0; i < 3; i++) {
            vector2[i] = sc.nextInt();
        }

        boolean tieneCero = false;
        for (int i = 0; i < 3; i++) {
            if (vector1[i] == 0 || vector2[i] == 0) {
                tieneCero = true;
                break;
            }
        }

        if (tieneCero) {
            System.out.println("Error: Uno o más elementos de los vectores son iguales a cero. El producto escalar no puede calcularse.");
        } else {
             int productoEscalar = 0;
            for (int i = 0; i < 3; i++) {
                productoEscalar += vector1[i] * vector2[i];
            }
            System.out.println("El producto escalar de los vectores es: " + productoEscalar);
        }

        sc.close();
    }
}