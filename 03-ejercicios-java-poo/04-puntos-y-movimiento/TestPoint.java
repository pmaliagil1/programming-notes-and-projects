package Ejercicio9;
public class TestPoint {
    public static void main(String[] args) {
        Point p1 = new Point(1.0f, 2.0f);
        System.out.println(p1);

        MovablePoint mp1 = new MovablePoint(1.0f, 2.0f, 3.0f, 4.0f);
        System.out.println(mp1);

        mp1.move();
        System.out.println(mp1);
    }
}