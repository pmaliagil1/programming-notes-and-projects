package EjerciciosClase.EjerciciosExplicacioes.ActividadesPresentacion;

import java.util.Random;

public class SimuladorDadoActividad1 {
    public static void main(String[] args) {

        Random rnd = new Random();
        int num = rnd.nextInt(6)+1;

        System.out.println(num);

    }
}
