package TareaNavidad;

import java.util.Scanner;

public class LaTreceCatorce {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner (System.in);
        
        int casos = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0; i < casos; i++){
            String[] partes = sc.nextLine().split("-");
            int a = Integer.parseInt(partes[0]);
            int b = Integer.parseInt(partes[1]);

            if (a - b == 1 ) {
               if (b % 2 == 0){
                System.out.println("SI");
               }else {
                System.out.println("NO");
               }
            } else if (b - a == 1){
                if (a % 2 == 0){
                    System.out.println("SI");
                }else {
                    System.out.println("NO");
                }
            } else {
                System.out.println("NO");
            }


        }
        sc.close();
    }
}
