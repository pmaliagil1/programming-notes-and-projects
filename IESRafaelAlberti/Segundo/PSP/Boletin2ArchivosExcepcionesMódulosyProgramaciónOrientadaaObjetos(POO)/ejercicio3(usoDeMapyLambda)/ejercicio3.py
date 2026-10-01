"""3. Mapeo con lambda y map: Dada una lista de temperaturas en Celsius [0, 15, 22,
30], usa map() y una función lambda para obtener una nueva lista conver<da a
Fahrenheit."""

celsius =  [0, 15, 22, 30]
fahrenheit = list(map(lambda temperatura: temperatura * 9 / 5 + 32, celsius))
print(fahrenheit)


