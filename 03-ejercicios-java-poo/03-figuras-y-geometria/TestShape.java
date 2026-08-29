package Ejercicio10;

public class TestShape {
    public static void main(String[] args) {
        Shape s1 = new Shape("blue", false);
        System.out.println(s1);

        Circle c1 = new Circle(5.5, "purple", true);
        System.out.println(c1);
        System.out.println("Area is " + c1.getArea());
        System.out.println("Perimeter is " + c1.getPerimeter());

        Rectangle r1 = new Rectangle(1.2, 3.4, "orange", false);
        System.out.println(r1);
        System.out.println("Area is " + r1.getArea());
        System.out.println("Perimeter is " + r1.getPerimeter());

        Square sq1 = new Square(6.6, "yellow", true);
        System.out.println(sq1);
        System.out.println("Area is " + sq1.getArea());
        System.out.println("Perimeter is " + sq1.getPerimeter());
    }
}