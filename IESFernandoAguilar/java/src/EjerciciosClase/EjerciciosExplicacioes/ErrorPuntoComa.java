package EjerciciosClase.EjerciciosExplicacioes;
public class ErrorPuntoComa {
    public static void main(String[] args) {
        int x = 1;
        if (x % 2 == 0); {   //por ese ; la sentencia de el print se ejecuta ya que dentro del if solo esta el ;
            System.out.println("x is even");
        }
    }
}
