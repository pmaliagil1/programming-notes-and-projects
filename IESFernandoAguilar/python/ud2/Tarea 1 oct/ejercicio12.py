total_pagado = 0
pago_mensual = 10
for mes in range (1, 21):
    total_pagado = total_pagado + pago_mensual
    print (f"Pago del mes {mes} : {pago_mensual} €")
    pago_mensual = pago_mensual * 2 
print(f"Total pagado después de 20 meses: {total_pagado} €")

