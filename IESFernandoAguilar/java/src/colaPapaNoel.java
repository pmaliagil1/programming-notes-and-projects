import java.util.Scanner;

public class colaPapaNoel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int casos = sc.nextInt();

        for (int i = 0; i < casos; i++) {
            int n = sc.nextInt();
            int a = sc.nextInt() - 1;

            int[] regalos = new int[n];
            for (int j = 0; j < n; j++) {
                regalos[j] = sc.nextInt();
            }

            int tiempo = 0;
            boolean terminado = false;

            while (!terminado) {
                for (int j = 0; j < n; j++) {
                    if (regalos[j] > 0) {
                        tiempo += 2;
                        regalos[j]--;

                        if (j == a && regalos[j] == 0) {
                            terminado = true;
                            break;
                        }
                    }
                }
            }

            System.out.println(tiempo);
        }

        sc.close();
    }
}
