package EjerciciosClase.EjerciciosExplicacioes;
import java.util.Scanner;
public class ActividadEntradaSalida {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dime un número");
        int num=sc.nextInt();


        System.out.println("Ahora dime un nombre");
        String cadena = sc.next();
        System.out.println("Has introducido el número: " + num + "y el nombre " + cadena);
        sc.close();
    }

}
