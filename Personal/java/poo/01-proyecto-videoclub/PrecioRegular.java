public class PrecioRegular extends Precio {


    @Override
    public  int getCodigoPrecio(){
        return Precio.REGULAR;
    }
    @Override
    public  double getImporte(int diasAlquilado){
        double importe=2;
        if(diasAlquilado>2){
            importe += (diasAlquilado -2)*1.5;
        }
        return importe;
    }

}
