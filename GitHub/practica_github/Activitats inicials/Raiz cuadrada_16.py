#Importamos la librería math para usar la función sqrt
import math
sqrt=math.sqrt
#Pedimos un número al usuario, calculamos su raíz cuadrada, la dividimos entre 2 y mostramos el resultado redondeado
num=float(input("Introduce el valor del número"))
raiz=(sqrt(num))
resultado=round(raiz/2,0)
print("La raíz cuadrada dividida entre 2 de tu número es:", resultado)
