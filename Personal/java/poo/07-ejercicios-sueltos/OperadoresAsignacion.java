package EjerciciosClase.EjerciciosExplicacioes;
public class OperadoresAsignacion {
    public static void main(String[] args) {
        
        double capital = 500.0;
        double interes = 6.25;

        double rentaSimple;

        rentaSimple = capital*interes/100;

        capital += rentaSimple;

        System.out.println("Interes = " + rentaSimple);
        System.out.println("Acumulado = " + capital);
    }
}
