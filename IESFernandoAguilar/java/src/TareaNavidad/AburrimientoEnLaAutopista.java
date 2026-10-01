package TareaNavidad;

import java.util.Scanner;

public class AburrimientoEnLaAutopista {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int casos = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < casos; i++) {
            int viejos = 0;
            int nuevos = 0;
            String matriculaEdu = sc.next();
            String matricula = "";
            String numerosEdu = matriculaEdu.substring(0, 4);
            String letrasEdu = matriculaEdu.substring(4);
            int numeroRealEdu = Integer.parseInt(numerosEdu);

            while (!matricula.equals("0")) {
                matricula = sc.next();
                if (matricula.equals("0")) break;

                String matriculaCoche = matricula.substring(0, 4);
                String letrasCoche = matricula.substring(4);
                int numeroRealCoche = Integer.parseInt(matriculaCoche);

                if (letrasEdu.compareTo(letrasCoche) < 0) {
                    viejos++;
                } else if (letrasEdu.compareTo(letrasCoche) > 0) {
                    nuevos++;
                } else {
                    if (numeroRealEdu > numeroRealCoche) {
                        nuevos++;
                    } else if (numeroRealEdu < numeroRealCoche) {
                        viejos++;
                    }
                }
            }
            System.out.printf("%d %d%n", nuevos, viejos);
        }
        sc.close();
    }
}
