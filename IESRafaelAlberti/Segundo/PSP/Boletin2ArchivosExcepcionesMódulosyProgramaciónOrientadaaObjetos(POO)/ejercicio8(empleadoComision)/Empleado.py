class Empleado:

    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base


    def calcular_salario(self):
        return self.salario_base