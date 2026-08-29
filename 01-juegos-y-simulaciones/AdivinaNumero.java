package EjerciciosPuente;
import java.util.Scanner;
import java.util.Random;
public class AdivinaNumero {
    public static void main(String[] args) {
        System.out.println("Bienvenido a 'adivina el número'");
        System.out.println("Estoy pensando en un número entre 1 y 20");
        System.out.println("Trata de adivinarlo en no más de 6 intentos");
        
        Random rd=new Random();
        int num=rd.nextInt(20)+1;
        Scanner sc=new Scanner(System.in);
        int numero=21;
        int contador = 0;
        while (num != numero){
            contador += contador;
            System.out.println("Adivina");
            numero = sc.nextInt();
            if (numero < num) {
                System.out.println("Es muy bajo");
            }else {
                System.out.println("Es muy alto");
            }
        }
        if (num  == numero){
            System.out.println("Buen trabajo, has adivinado en " + contador + " intentos");
        }
        
        sc.close();
    }
}



