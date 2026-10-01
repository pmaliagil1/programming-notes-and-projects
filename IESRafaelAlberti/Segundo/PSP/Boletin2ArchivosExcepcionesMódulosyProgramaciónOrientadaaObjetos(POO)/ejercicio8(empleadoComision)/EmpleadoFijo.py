from Empleado import Empleado

class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, salario_base: float):
        super().__init__(nombre, salario_base)

    def calcular_salario(self):
        return self.salario_base