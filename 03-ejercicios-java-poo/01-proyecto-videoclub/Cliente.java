
import java.util.ArrayList;
import java.util.List;

public class Cliente {

    private String nombre;
    private List<Alquiler> alquileres = new ArrayList<>();

    public Cliente(String nombre) {
        this.nombre = nombre;
    }

    public void agregarAlquiler(Alquiler alquiler) {
        alquileres.add(alquiler);
    }

    public String getNombre() {
        return nombre;
    }

    public String extracto() {
        double importeTotal = 0;
        int puntosFrecuentes = 0;
        String resultado = "Alguileres de " + getNombre() + "\n";

        for (Alquiler alquiler : alquileres) {
            double importe = alquiler.getImporte();
            puntosFrecuentes += alquiler.getPuntosFrecuentes();

            resultado += "\t" + alquiler.getPelicula().getTitulo() + "\t" + String.valueOf(importe) + "\n";
            importeTotal += importe;
            // determine amounts for each line

        }

        // add footer lines
        resultado += "Cantidad adecuada: " + String.valueOf(importeTotal) + "\n";
        resultado += "Has ganado " + String.valueOf(puntosFrecuentes) + " puntos del alquiler frecuente";

        return resultado;
    }
}