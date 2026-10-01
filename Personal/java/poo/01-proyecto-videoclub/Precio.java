public abstract class Precio {

    public static final int INFANTIL = 2;
    public static final int ESTRENO = 1;
    public static final int REGULAR = 0;

    public abstract int getCodigoPrecio();

    public abstract double getImporte(int diasAlquilado);

    public int getPuntosFrecuentes(int diasAlquilado) {
        return 1;
    }

}
