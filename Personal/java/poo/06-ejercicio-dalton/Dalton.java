package EjerciciosPuente;
import java.util.Scanner;

public class Dalton {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hermanos = sc.nextInt();

        while (hermanos != 0) {
            int anterior = sc.nextInt();

            boolean ascendente = true;
            boolean descendente = true;


            for (int i = 1; i < hermanos; i++) {
                int actual = sc.nextInt();

                if (actual > anterior) {
                    descendente = false;
                } else if (actual < anterior) {
                    ascendente = false;
                }

                anterior = actual;
            }

            if (ascendente || descendente) {
                System.out.println("DALTON");
            } else {
                System.out.println("DESCONOCIDOS");
            }
            hermanos = sc.nextInt();
        }

    }
}
