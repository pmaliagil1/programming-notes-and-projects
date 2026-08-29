package TareaCasa;

import java.util.Scanner;

public class PrimoDeRiesgo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int casosDePrueba = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < casosDePrueba; i++) {
            String palabra = sc.nextLine();

            int sumaASCII = 0;
            for (int j = 0; j < palabra.length(); j++) {
                sumaASCII += (int) palabra.charAt(j);
            }

        }

        sc.close();
    }

    private static int encontrarPrimoInferior(int numero) {
        for (int i = numero; i > 1; i--) {
            if (esPrimo(i)) {
                return i;
            }
        }
        return 2;
    }

    private static boolean esPrimo(int numero) {
        if (numero < 2) {
            return false;
        }

            }
        }
        return true;
    

