package EjerciciosClase.EjerciciosExplicacioes.ActividadesPresentacion;

import java.util.Random;
import java.util.Scanner;

public class NumerosAlActividad2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rd = new Random();

        boolean continuar = true;

        while (continuar) {
            int numero1 = rd.nextInt(100) + 1;
            int numero2 = rd.nextInt(100) + 1;
            int operacion = 0;
            String operador = "";

            int opcionOperacion = rd.nextInt(4);

            if (opcionOperacion == 0) {
                operacion = numero1 + numero2;
                operador = "+";
            } else if (opcionOperacion == 1) {
                operacion = numero1 - numero2;
                operador = "-";
            } else if (opcionOperacion == 2) {
                operacion = numero1 * numero2;
                operador = "*";
            } else if (opcionOperacion == 3) {
                while (numero2 == 0) {
                    numero2 = rd.nextInt(100) + 1;
                }
                operacion = numero1 / numero2;
                operador = "/";
            }

            System.out.println(numero1 + " " + operador + " " + numero2 + " = ?");

            int respuestaUsuario = sc.nextInt();

            if (respuestaUsuario == operacion) {
                System.out.println("CORRECTO");
                continuar = false;
            } else {
                System.out.println("INCORRECTO. Inténtalo de nuevo.");
            }
        }

        sc.close();
    }
}


