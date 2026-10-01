import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class referenciasCruzadas {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int n = Integer.parseInt(scanner.nextLine());
            if (n == 0) break;

            Map<String, Set<Integer>> referencias = new TreeMap<>();

            for (int i = 1; i <= n; i++) {
                String linea = scanner.nextLine().toLowerCase();
                String[] palabras = linea.split("\\W+");

                for (String palabra : palabras) {
                    if (palabra.length() > 2) {
                        referencias.putIfAbsent(palabra, new TreeSet<>());
                        referencias.get(palabra).add(i);
                    }
                }
            }

            for (Map.Entry<String, Set<Integer>> entrada : referencias.entrySet()) {
                System.out.print(entrada.getKey() + " ");
                for (int linea : entrada.getValue()) {
                    System.out.print(linea + " ");
                }
                System.out.println();
            }

            System.out.println("----");
        }

        scanner.close();
    }
}