#Importamos la librería math para usar el valor de pi
import math
pi = math.pi
#Pedimos el radio de la circunferencia al usuario y calculamos su área y perímetro
r = float(input("Introdueix el radi de la circumferència: "))
area = round(pi * r * r,2)
perimetro = round(2 * pi * r, 2)
print("L'àrea de la circumferència és: ", area, "i el perímetre és: ", perimetro)  