fun main(){
    val t: Tecnico = Tecnico("111F","Emanuel", "xxx",2000.0,5)
    val c: Comercial = Comercial("222F","Manuela","yyy",1000.0,50.0)

    val empresa = Plantilla()

    empresa.contratarEmpleado(t)
    empresa.contratarEmpleado(c)

    val lista = empresa.getEmpleadosPorNombre("anu") //es comun en ambos nombres
    lista.forEach { println(it) }
}