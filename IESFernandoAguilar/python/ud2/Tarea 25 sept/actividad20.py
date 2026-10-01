mes = int(input("Introduce un número entre 1 y 12 para conocer el número de días del mes: "))
if mes == 1:  
    dias = 31
    print(f"El mes {mes} (enero) tiene {dias} días.")
elif mes == 2:  
    dias = 28  
    print(f"El mes {mes} (febrero) tiene {dias} días.")
elif mes == 3:  
    dias = 31
    print(f"El mes {mes} (marzo) tiene {dias} días.")
elif mes == 4: 
    dias = 30
    print(f"El mes {mes} (abril) tiene {dias} días.")
elif mes == 5:
    dias = 31
    print(f"El mes {mes} (mayo) tiene {dias} días.")
elif mes == 6: 
    dias = 30
    print(f"El mes {mes} (junio) tiene {dias} días.")
elif mes == 7:  
    dias = 31
    print(f"El mes {mes} (julio) tiene {dias} días.")
elif mes == 8: 
    dias = 31
    print(f"El mes {mes} (agosto) tiene {dias} días.")
elif mes == 9:  
    dias = 30
    print(f"El mes {mes} (septiembre) tiene {dias} días.")
elif mes == 10:  
    dias = 31
    print(f"El mes {mes} (octubre) tiene {dias} días.")
elif mes == 11: 
    dias = 30
    print(f"El mes {mes} (noviembre) tiene {dias} días.")
elif mes == 12:  
    dias = 31
    print(f"El mes {mes} (diciembre) tiene {dias} días.")
else:
    print ("El número debe ser entre 1 y 12")  