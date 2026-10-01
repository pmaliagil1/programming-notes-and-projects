/*Tienes este código:
palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)
Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda
aceptar una cadena y una letra como argumentos. De tal forma que pueda hacer la
siguiente llamada:
numero_de_os = cuenta("consuelo","o") # Resultado debe ser 2*/

fun main(){
    val palabra: String ?
    val cadenaLambda = {frase: String, l: Char -> frase.filter { it == l }.length}
    println(cadenaLambda("Consuelo tiene un pañuelo", 'o'))
}