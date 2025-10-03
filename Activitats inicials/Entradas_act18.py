#Calculamos el precio de las entradas a un parque de atracciones según la edad de las personas
Menores=int(input("Introduce el número de menores de 18 años: "))
Mayores=int(input("Introduce el número de mayores de 18 años: "))
Personas=Menores+Mayores
Precio_menores=Menores*12*0.5
Precio_mayores=Mayores*12*0.9
Precio_entradas= Precio_menores+Precio_mayores
print("El precio total de las entradas es:", Precio_entradas, "€" "Precio de",Menores,"menores, es de:",Precio_menores,"€" "Precio de",Mayores,"mayores, es de:",Precio_mayores,"€")

