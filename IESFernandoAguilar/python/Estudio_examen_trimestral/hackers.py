def encontrarHackersInteligentes(correos):
    # Extraer dominios de los correos
    dominios = [correo.split('@')[-1] for correo in correos]
    
    # Contar cuántas veces aparece cada dominio manualmente
    conteo_dominios = {}
    for dominio in dominios:
        if dominio in conteo_dominios:
            conteo_dominios[dominio] += 1
        else:
            conteo_dominios[dominio] = 1
    
    # Encontrar el dominio que más veces se repite
    maximo_conteo = max(conteo_dominios.values())
    dominios_sospechosos = [dominio for dominio, conteo in conteo_dominios.items() if conteo == maximo_conteo]
    
    # Filtrar los correos que pertenecen a los dominios sospechosos
    correos_sospechosos = [correo for correo in correos if correo.split('@')[-1] in dominios_sospechosos]
    
    return correos_sospechosos

# Lista de entrada
correos = [
    'hola@somoshackersastutos.com',
    'ambrosio@outlook.com',
    'coco@malandriners.dev',
    'hello@somoshackersastutos.com',
    'ambrosio@outlook.com',
    'ciao@somoshackersastutos.com'
]

# Llamada a la función y salida
hackers = encontrarHackersInteligentes(correos)
print(hackers)