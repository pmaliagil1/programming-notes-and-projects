"""Dadas las siguientes listas:
frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
1. Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y 
set_frutas2.
2. Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto 
llamado frutas_comunes.
3. Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un 
conjunto llamado frutas_solo_en_frutas1.
4. Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un 
conjunto llamado frutas_solo_en_frutas2.
5. Encuentra las frutas que están en frutas 1 pero no en frutas 2 y los que están en 
frutas 2 pero no están en frutas 1. Guárdalas en un conjunto llamado frutas_raras"""

def frutas(frutas1, frutas2):
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)       #1º
    frutas_comunes = set_frutas1.intersection(set_frutas2)      #2º
    frutas_solo_en_frutas1 = set_frutas1.difference(set_frutas2)        #3º
    frutas_solo_en_frutas2 = set_frutas2.difference(set_frutas1)        #4º
    frutas_raras = set_frutas1 ^ set_frutas2        #5º

    return f"{frutas_comunes}\n{frutas_solo_en_frutas1}\n{frutas_solo_en_frutas2}\n{frutas_raras}"

     

if __name__ == "__main__":
    try:
        frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
        frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
        print(frutas(frutas1,frutas2))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")