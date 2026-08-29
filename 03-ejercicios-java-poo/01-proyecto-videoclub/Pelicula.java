
public class Pelicula {

    private String titulo;
    private Precio precio;

    public Pelicula(String titulo, int tipoPrecio) {
        this.titulo = titulo;
        setCodigoPrecio(tipoPrecio);
    }

    public int getCodigoPrecio() {
        return precio.getCodigoPrecio();
    }

    public void setCodigoPrecio(int codigoPrecio) {
        switch (codigoPrecio) {
            case Precio.INFANTIL:
                precio = new PrecioInfantil();
                break;
            case Precio.ESTRENO:
                precio = new PrecioEstreno();
                break;
            case Precio.REGULAR:
                precio = new PrecioRegular();
                break;

            default:
                throw new IllegalArgumentException("Codigo de precio no válido");
        }
    }

    public String getTitulo() {
        return titulo;
    }

    public double getImporte(int diasAlquilados) {
        return precio.getImporte(diasAlquilados);
    }

    public int getPuntosFrecuentes(int diasAlquilado) {
        return precio.getPuntosFrecuentes(diasAlquilado);
    }
}