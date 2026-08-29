package clases;

public class testDate {
    public static void main(String[] args) {
        date date = new date(1, 1, 2024);

        System.out.println("Fecha inicial: " + date.toString());

        date.setDay(15);
        date.setMonth(6);
        date.setYear(2025);

        System.out.println("Fecha modificada: " + date.toString());

        System.out.println("Día: " + date.getDay());
        System.out.println("Mes: " + date.getMonth());
        System.out.println("Año: " + date.getYear());

        date.setDate(31, 12, 2026);
        System.out.println("Fecha establecida con setDate: " + date.toString());
    }
}