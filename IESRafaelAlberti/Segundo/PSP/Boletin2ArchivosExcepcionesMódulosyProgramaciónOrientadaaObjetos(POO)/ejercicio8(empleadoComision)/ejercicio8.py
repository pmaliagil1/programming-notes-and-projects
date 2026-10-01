"""8. Herencia y Polimorfismo: Crea una clase base Empleado con método
calcular_salario(). Hereda de ella para crear dos subclases: EmpleadoFijo (salario
base) y EmpleadoComision (salario base + ventas * comisión)."""

from Empleado import Empleado
from EmpleadoFijo import EmpleadoFijo
from EmpleadoComision import EmpleadoComision

emp1 = EmpleadoFijo("Ana", 2500)
emp2 = EmpleadoComision("Carlos", 1200, ventas=15000, comision=0.08)  # 1200 + 1200 = 2400

lista_empleados = [emp1, emp2]

# Demostración de Polimorfismo
for emp in lista_empleados:
    print(f"Empleado/a: {emp.nombre} -> Salario total: {emp.calcular_salario():.2f}€")