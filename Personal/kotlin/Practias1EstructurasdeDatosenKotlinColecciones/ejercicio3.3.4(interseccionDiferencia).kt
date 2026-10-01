/*Dadas las siguientes listas:
frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
1. Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y
set_frutas2.
2. Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto
llamado frutas_comunes.
3. Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un
conjunto llamado frutas_solo_en_frutas1.
4. Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un
conjunto llamado frutas_solo_en_frutas2*/

fun main() {
    val frutas1 = listOf("manzana", "pera", "naranja", "plátano", "uva")
    val frutas2 = listOf("manzana", "pera", "durazno", "sandía", "uva")

    // 1. Crear conjuntos
    val set_frutas1 = frutas1.toSet()
    val set_frutas2 = frutas2.toSet()

    // 2. Comunes (Intersección)
    val frutas_comunes = set_frutas1.intersect(set_frutas2)

    // 3. Solo en frutas1 (Diferencia)
    val frutas_solo_en_frutas1 = set_frutas1.subtract(set_frutas2)

    // 4. Solo en frutas2 (Diferencia)
    val frutas_solo_en_frutas2 = set_frutas2.subtract(set_frutas1)

    // Mostrar resultados
    println("Set 1: $set_frutas1")
    println("Set 2: $set_frutas2")
    println("Frutas comunes: $frutas_comunes")
    println("Frutas solo en frutas1: $frutas_solo_en_frutas1")
    println("Frutas solo en frutas2: $frutas_solo_en_frutas2")
}
