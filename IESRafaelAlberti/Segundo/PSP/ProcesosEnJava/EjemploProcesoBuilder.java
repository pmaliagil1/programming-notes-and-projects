import java.io.File;
import java.io.IOException;
public class EjemploProcesoBuilder{
    public static void main(String[] args) {
        try{
            ProcessBuilder pb = new ProcessBuilder("ping","-c","3","8.8.8.8");//Windows: "-n"
            pb.directory(new File(System.getProperty("user.home")));// carpeta de trabajo
            pb.environment().put("MODO","prueba");          //variable de entorno
            pb.inheritIO();                   //el hijo escribe en nuestra consola

            Process p = pb.start();        //puede lanzar IOException
            System.out.println("PID el hijo: "+p.pid());

            int codigo = p.waitFor();     //bloquea hasta que termina
            System.out.println("Terminó con código "+codigo); //0=todo bien
            
        } catch(IOException | InterruptedException e){
            
        }
    }
}