
public class PruebaVideoclub {

    public static void main(String[] args) {
        Pelicula pelicula1 = new Pelicula("Madagascar", Precio.INFANTIL);
        Alquiler alquiler1 = new Alquiler(pelicula1, 6); // 6 day rental
        Pelicula pelicula2 = new Pelicula("Star Wars", Precio.ESTRENO);
        Alquiler alquiler2 = new Alquiler(pelicula2, 2); // 2 day rental
        Pelicula pelicula3 = new Pelicula("Gone with the Wind", Precio.REGULAR);
        Alquiler alquiler3 = new Alquiler(pelicula3, 8); // 8 day rental
        Cliente cliente1 = new Cliente("David");
        cliente1.agregarAlquiler(alquiler1);
        cliente1.agregarAlquiler(alquiler2);
        cliente1.agregarAlquiler(alquiler3);
        System.out.println(cliente1.extracto());
    }
}