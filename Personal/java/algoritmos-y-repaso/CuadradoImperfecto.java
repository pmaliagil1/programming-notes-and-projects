package TareaCasa;
import java.util.Scanner;
public class CuadradoImperfecto {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        boolean mayor = false;
        
        if (num > 10){
            do{
                num = num - 10;
            }   while (num > 10);
            mayor = true;
        }
        if (num == 0 || num == 1 || num == 4 || num == 9 && mayor){
            System.out.println("IMPERFECTO");
        }else{
            System.out.println("NO SE");
        }
        sc.close();
        }
       
    }


