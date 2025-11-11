#importamos la librería math para usar el valor de pi
import math
pi= math.pi
#Pedimos el radio y la altura del cilindro al usuario y calculamos su área y volumen
radi=float(input("Introduce el radio de la base del cilindro"))
altura=float(input("Introduce la altura del cilindro"))
area_base= round(pi * radi * radi,2)
area_lateral= round(2 * pi * radi * altura,2)   
volumen= round(area_base * altura,2)
area_total= round(2 * area_base + area_lateral,2)
print("El área del cilindro es: ", area_total, " y el volumen es: ", volumen,) 
