import math
lado=float(input("Introduce el valor de un lado"))
sqr=math.sqrt(3)
area=round(sqr/4*lado**2,2)
print("El área de un triángulo equilatero de lados de", lado,"cm es", area)