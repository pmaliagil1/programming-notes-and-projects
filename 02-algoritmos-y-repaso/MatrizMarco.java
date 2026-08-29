package matriz;

import java.util.Scanner;

public class MatrizMarco {
    public static void imprimir_matriz(int [][]matriz) {
        for (int i = 0; i<matriz.length;i++){
            for (int x=0;x<matriz.length;x++){
                if (x == 0 || i == 0 || x == matriz[i].length - 1 || i == matriz.length - 1){
                    matriz[i][x] = 1;
                }else{
                    matriz[i][x] = 0;
                }
                System.out.print(" " + matriz[i][x]);
            }
            System.out.println();

        }

    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dime las filas de la matriz");
        int dimension_n = sc.nextInt();
        System.out.println("Dime las columnas de la matriz");
        int dimension_m = sc.nextInt();
        int [][] matriz = new int[dimension_n][dimension_m];
        imprimir_matriz(matriz);

        sc.close();    

    }
}

