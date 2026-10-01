"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por
pantalla los créditos de cada asignatura en el formato <asignatura> tiene
<créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso,
y <créditos> son sus créditos. Al final debe mostrar también el número total de
créditos del curso."""

def creditoAsignaturas(asignaturas):
    suma_creditos = 0
    for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} tiene {creditos} créditos.")
        suma_creditos+=creditos
    print(f"Tienes un total de {suma_creditos} créditos")


if __name__ == "__main__":
    try:
        asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
        creditoAsignaturas(asignaturas)
    except Exception as e:
        print(f"Algo ha salido mal: {e}")