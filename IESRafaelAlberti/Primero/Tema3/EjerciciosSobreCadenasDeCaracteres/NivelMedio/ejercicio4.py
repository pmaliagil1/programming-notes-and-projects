"""Hay un método de cadenas llamado find, que es similar a count. Lee la documentación
de este método en:
• Métodos en ingles
• Métodos en castellano
Escribe el código necesario para invocar a este método find y contar el número de
veces que una letra aparece en “banana”."""


frase = "banana"
objetivo = "a"
contador = 0

indice = frase.find(objetivo)

while indice != -1:
    contador += 1
    indice = frase.find(objetivo, indice + 1)

print(f"La letra '{objetivo}' aparece {contador} veces.")