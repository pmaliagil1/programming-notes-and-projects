import java.util.Scanner;
public class sietePicos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true) {
            int cantidad = sc.nextInt();
            if (cantidad == 0)
            break;

            int[] alturas = new int [cantidad];
            for (int i = 0; i< alturas.length; i++)
                alturas[i] = sc.nextInt();

            int picos = 0;
            int n = alturas.length;

            int siguiente = 1;
            int anterior = alturas[alturas.length-1];
            boolean esPico = true;
            for (int i = 0;i < n;i++) {
                if (i == 0){
                    siguiente = alturas [i+1];
                    anterior = alturas[n-1];
                } else if (i == n - 1){
                    siguiente = alturas[0];
                    anterior = alturas[i-1];
                } else {
                    siguiente = alturas[i+1];
                    anterior = alturas[i-1];
                }
                
                esPico = alturas[i] > anterior && alturas[i] > siguiente;
                
                if (esPico)
                    picos++;
            }
            System.out.println(picos);
            sc.nextLine();
        }
    }
}