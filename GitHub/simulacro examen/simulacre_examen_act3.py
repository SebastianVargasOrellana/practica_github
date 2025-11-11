import math
radio_cilindro=float(input("Introduce el radio del cilindro: "))
altura_cilindro=float(input("Introduce la altura del cilindro: "))
pi=math.pi
volumen_cilindro=pi*radio_cilindro**2*altura_cilindro
caracteres=input("Quieres la respuesta en mayusculas o minúsculas? (M/m): ")
if caracteres=="M":
    print("EL VOLUMEN DEL CILINDRO ES: ", volumen_cilindro)
elif caracteres=="m":
    print("el volumen del cilindro es: ", volumen_cilindro)
else:
    print("Caracter no válido")
