from Empleado import Empleado

class EmpleadoComision(Empleado):
    def __init__(self, nombre: str, salario_base: float, ventas: float, comision: float):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.comision)