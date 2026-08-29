def ecuacionSegundoGrado(a, b, c):

    if a == 0:
        return "No es una ecuación de segundo grado"

    discriminante = (b**2 - 4 * a * c)

    if discriminante < 0:
        return None, None


    x1 = (-b + discriminante**0.5) / (2 * a)
    x2 = (-b - discriminante**0.5) / (2 * a)

    return x1, x2