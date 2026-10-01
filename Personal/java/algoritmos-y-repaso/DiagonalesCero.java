package matriz;

import java.util.Scanner;

public class DiagonalesCero {

    public static void imprimir_matriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(" " + matriz[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce el tamaño de la matriz cuadrada:");
        int n = sc.nextInt();

        int[][] matriz = new int[n][n];
        System.out.println("Introduce los valores de la matriz:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matriz[i][j] = sc.nextInt();
            }
        }

        System.out.println("Matriz original:");
        imprimir_matriz(matriz);

        for (int i = 0; i < n; i++) {
            matriz[i][i] = 0;
            matriz[i][n - 1 - i] = 0;
        }

        System.out.println("Matriz con diagonales en cero:");
        imprimir_matriz(matriz);

        sc.close();
    }
}
