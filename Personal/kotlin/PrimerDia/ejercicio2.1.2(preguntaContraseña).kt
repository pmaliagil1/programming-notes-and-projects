/*Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.*/

fun main(){

    val passwordGuardada: String = "alberti"

    print("Introduce una contraseña:")
    val passwordUsuario = readLine()?.lowercase()

    if (passwordUsuario != null && passwordUsuario.equals(passwordGuardada)) {
        println("La contraseña es CORRECTA")

    }else{
        println("La contraseña es INCORRECTA")
    }


}