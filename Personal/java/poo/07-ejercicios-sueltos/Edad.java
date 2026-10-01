package EjerciciosClase.EjerciciosExplicacioes;
import java.util.Scanner;
public class Edad {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(("Dime tu edad"));  
        int edad = sc.nextInt();
        if (edad>=18) 
            System.out.println("Eres mayor de edad, puedes votar");
        else
            System.out.println("Eres menor de edad, no puedes votar");
        
        sc.close();
        }

    }

