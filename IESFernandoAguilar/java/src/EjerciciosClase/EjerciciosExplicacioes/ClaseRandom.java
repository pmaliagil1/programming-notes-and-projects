package EjerciciosClase.EjerciciosExplicacioes;

import java.util.Random;

public class ClaseRandom {
    public static void main(String[] args) {
        
        Random rnd = new Random();

        int al = rnd.nextInt();
        System.out.println(al);

        float a2 = rnd.nextFloat();
        System.out.println(a2);

        double a3 = rnd.nextDouble();
        System.out.println(a3);

        long a4 = rnd.nextLong();
        System.out.println(a4);

        boolean a5 = rnd.nextBoolean();
        System.out.println(a5);
    }
}
