package EjerciciosPuente;

import java.util.Scanner;

public class PiramideCanicas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int casos = sc.nextInt();

        for (int i = 0; i < casos; i++) {
            int altura = sc.nextInt();
            long totalCanicas = 0;

            for (int j = 1; j <= altura; j++) {
                totalCanicas += (long) j * (j + 1) / 2;
            }

            System.out.println(totalCanicas);
        }

    }
}
