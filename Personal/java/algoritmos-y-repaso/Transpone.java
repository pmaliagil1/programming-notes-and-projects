package matriz;


import java.util.Scanner;

public class Transpone {

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

        // Leer dimensiones de la matriz
        System.out.println("Dime las filas de la matriz:");
        int n = sc.nextInt();
        System.out.println("Dime las columnas de la matriz:");
        int m = sc.nextInt();

        // Crear la matriz original
        int[][] matriz = new int[n][m];
        System.out.println("Introduce los valores de la matriz:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matriz[i][j] = sc.nextInt();
            }
        }

        // Crear la matriz traspuesta
        int[][] traspuesta = new int[m][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                traspuesta[j][i] = matriz[i][j];
            }
        }

        // Mostrar la matriz original
        System.out.println("Matriz original:");
        imprimir_matriz(matriz);

        // Mostrar la matriz traspuesta
        System.out.println("Matriz traspuesta:");
        imprimir_matriz(traspuesta);

        sc.close();
    }
}