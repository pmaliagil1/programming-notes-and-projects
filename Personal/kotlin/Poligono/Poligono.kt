abstract class Poligono { //es abstracta cuando no se dice como se implementa, en cada hijo se implementa de forma diferente

    init {
        contadorPoligonos++
    }
    companion object { //sirve para hacer una variable global y poder acceder desde cualquier clase
        var contadorPoligonos: Int = 0
    }

    abstract fun perimetro(): Int
    abstract fun area(): Int

}