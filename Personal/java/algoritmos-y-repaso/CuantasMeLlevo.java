package TareaCasa;
import java.util.Scanner;

public class CuantasMeLlevo {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int num1 = 1;
        int num2 = 1;
        int digitoAnterior1;
        int digitoAnterior2;
        int sumaDigito;
        int meLlevo = 0;

        while (num1 != 0 && num2 != 0){ 
            
            num1 = sc.nextInt();
            num2 = sc.nextInt();

            if (num1 != 0 && num2 != 0){

                for(int contador = 1 ; contador<=3 ; contador++){

                    digitoAnterior1 = num1 % 10;
                    digitoAnterior2 = num2 % 10;
                    num1 = num1/10;
                    num2 = num2/10;
                    sumaDigito = digitoAnterior1+digitoAnterior2;
    
                    if(sumaDigito >= 10){
                        meLlevo ++;
                    }
                    sumaDigito = 0;
                }
                System.out.println(meLlevo);
                meLlevo = 0;
                num1 = 1;
                num2 = 1;
            }
            
        }

    }
}