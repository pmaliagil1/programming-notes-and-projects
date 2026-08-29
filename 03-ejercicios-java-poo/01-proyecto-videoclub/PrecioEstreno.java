public class PrecioEstreno extends Precio {
    @Override
    public  int getCodigoPrecio(){
        return Precio.ESTRENO;
    }

    @Override
    public  double getImporte(int diasAlquilado){
        double importe=diasAlquilado *3;
        
        return importe;
    }
    @Override
        public int getPuntosFrecuentes(int diasAlquilado){
            if(diasAlquilado > 1){
                return 2;
            }
            else{
                return 1;

            }

        }
}
