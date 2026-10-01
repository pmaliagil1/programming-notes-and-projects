package matriz;

import java.util.Scanner;

public class CuadradoMagico {

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

        System.out.println("Dime la dimensión de la matriz:");
        int dimension = sc.nextInt();

        int[][] matriz = new int[dimension][dimension];

        System.out.println("Introduce los valores de la matriz:");
        for (int i = 0; i <=          //no se hacerlo