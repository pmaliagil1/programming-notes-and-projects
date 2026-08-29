/**
 * The rental class represents a customer renting a movie.
 */
public class Alquiler {

    private Pelicula pelicula;
    private int diasAlquilada;

    public Alquiler(Pelicula pelicula, int diasAlquilada) {
        this.pelicula = pelicula;
        this.diasAlquilada = diasAlquilada;
    }

    public int getDiasAlquilada() {
        return diasAlquilada;
    }

    public Pelicula getPelicula() {
        return pelicula;
    }

    public double getImporte() {
        return pelicula.getImporte(diasAlquilada);
    }

    public int getPuntosFrecuentes() {
        return pelicula.getPuntosFrecuentes(diasAlquilada);
    }
}
