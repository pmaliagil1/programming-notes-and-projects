public class PrecioInfantil extends Precio {

    @Override
    public int getCodigoPrecio() {
        return INFANTIL;
    }

    @Override
    public double getImporte(int diasAlquilado) {
        double importe = 1.5;
        if (diasAlquilado > 3) {
            importe += (diasAlquilado - 3) * 1.5;
        }
        return importe;
    }

}
