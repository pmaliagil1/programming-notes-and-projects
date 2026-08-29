// TestResizableCircle.java
package Ejercicio15;

public class TestResizableCircle {
    public static void main(String[] args) {
        ResizableCircle resizableCircle = new ResizableCircle(7.0);
        System.out.println("Radio inicial del ResizableCircle: " + resizableCircle.getRadius());

        resizableCircle.resize(50); // Aumenta el radio en un 50%
        System.out.println("Radio después de redimensionar al 50%: " + resizableCircle.getRadius());

        resizableCircle.resize(-20); // Disminuye el radio en un 20%
        System.out.println("Radio después de redimensionar al -20%: " + resizableCircle.getRadius());
    }
}