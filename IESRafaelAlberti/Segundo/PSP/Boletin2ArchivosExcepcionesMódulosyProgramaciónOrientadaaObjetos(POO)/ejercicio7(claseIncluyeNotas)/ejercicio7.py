"""7. Clase Básica (POO): Diseña una clase Estudiante con los atributos nombre, edad
y notas (lista). Incluye métodos para añadir una nota y calcular la nota media del
estudiante."""
from Estudiante import Estudiante

estudiante1 = Estudiante("Pablo",21)

estudiante1.incluye_nota(8)
estudiante1.incluye_nota(5)


nota_final = estudiante1.calcular_media()
print(nota_final)