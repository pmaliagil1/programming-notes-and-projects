package EjerciciosClase;

import java.math.BigInteger;

public class EjemploUsoBigInteger {
    public static void main(String[] args) {
        BigInteger num1 = new BigInteger("7598485758848557844757");
        BigInteger num2 = new BigInteger("76854858756879576585768");

        BigInteger sum = num1.add(num2);
        BigInteger product = num1.multiply(num2);
        BigInteger gcd = num1.gcd(num2);

        System.out.println("Suma: " + sum);
        System.out.println("Producto: " + product);
        System.out.println("MCD: " + gcd);
    }
}
