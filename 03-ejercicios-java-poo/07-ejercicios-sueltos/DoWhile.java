package EjerciciosClase.EjerciciosExplicacioes;
import java.util.Scanner;
public class DoWhile {
    public static void main(String[] args) {
        
        Scanner teclado=new Scanner(System.in);
        int num;
        do{
            System.out.println("Introduce un número mayor que 100: ");
            num=teclado.nextInt();
        } while (num<=100);
        teclado.close();
}
}
