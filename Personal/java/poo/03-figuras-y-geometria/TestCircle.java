package Ejercicio15;

public class TestCircle {
    public static void main(String[] args) {
        Circle circle = new Circle(5.0);
        System.out.println("Radio del círculo: " + circle.getRadius());
        System.out.println("Perímetro del círculo: " + circle.getPerimeter());
        System.out.println("Área del círculo: " + circle.getArea());

        circle.setRadius(10.0);
        System.out.println("\nNuevo radio del círculo: " + circle.getRadius());
        System.out.println("Nuevo perímetro del círculo: " + circle.getPerimeter());
        System.out.println("Nueva área del círculo: " + circle.getArea());
    }
}