class Estudiante:
    def __init__ (self,nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.notas = []


    def incluye_nota(self,nota:float):
        if nota >0 and nota <11:
            self.notas.append(nota)
            print(f"Nota {nota} añadida")
        else:
            print("La nota debe ser entre 0 y 10")

    def calcular_media(self):
        if not self.notas:
            return("No hay notas disponibles")
        else:
            media = sum(self.notas) / len(self.notas)
            return media