#Pedimos el dividendo y el divisor al usuario, realizamos la división y mostramos si el dividendo es par o impar
divisor=float(input("Introduce el divisor: "))
dividendo=float(input("Introduce el dividendo: "))
cociente=dividendo/divisor
resto=dividendo%divisor
if dividendo%2==0:
    print ("El cociente és: ",cociente,", el resto és: ",resto, "i el dividendo es par")
else:
    print ("El cociente és: ",cociente,", el resto és: ",resto, "i el dividendo es impar")