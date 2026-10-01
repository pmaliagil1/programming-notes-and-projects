package EjerciciosPuente;

import java.util.Scanner;

public class AreaRectangulo {

public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {

            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            
            if (x2 < x1 || y2 < y1) {
                break;
            }
            int area = (x2 - x1) * (y2 - y1);

            System.out.println(area);
        }
        sc.close();
    }
}
