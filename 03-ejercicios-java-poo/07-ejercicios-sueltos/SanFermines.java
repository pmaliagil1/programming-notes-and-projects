import java.util.Scanner;

public class SanFermines {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNext()) {

            int n = sc.nextInt();
            
            if (n == 0) {
                break;
            }
            
            int maxVelocidad = 0;

            for (int i = 0; i < n; i++) {
                int velocidad = sc.nextInt();
                if (velocidad > maxVelocidad) {
                    maxVelocidad = velocidad;
                }
            }

            System.out.println(maxVelocidad);
        }
        sc.close();
    }
}
