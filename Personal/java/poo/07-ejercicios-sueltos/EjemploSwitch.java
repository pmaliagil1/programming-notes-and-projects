package EjerciciosClase.EjerciciosExplicacioes;
import java.util.Scanner;
public class EjemploSwitch {
    public static void main(String[] args) {
        
            Scanner sc=new Scanner(System.in);
            System.out.println("Introduce el número de mes: ");
            short mes = sc.nextShort();
            switch (mes) {
                case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                    System.out.println("el mes número " + mes + " tiene 31 días");
                    break;
                case 2:
                    System.out.println("el mes número " + mes + " tiene 29 días");
                    break;
                case 4: case 6: case 9: case 11:
                    System.out.println("el mes número " + mes + " tiene 30 días");
                    break;
                default:
                    System.out.println("Mes inexistente");
            }
            sc.close();
    }
}
