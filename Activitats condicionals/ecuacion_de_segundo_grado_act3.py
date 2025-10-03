## Ejercicio 3
a=float(input("Introduce el valor de a:"))
b=float(input("Introduce el valor de b:"))
c=float(input("Introduce el valor de c:"))
#calculo el valor de la raiz cuadrada
raizcuadrada=b**2-4*a*c
#utilizo una condición para ver si la raiz cuadrada es negativa, positiva o cero
if raizcuadrada<0:
    print("La ecuacion no tiene solucion en los reales")
#si la raiz cuadrada es 0 o positiva, calculo las dos soluciones
elif raizcuadrada>=0:
    raizcuadrada=b**2-4*a*c
    x1=(-b+raizcuadrada**0.5)/(2*a)
    x2=(-b-raizcuadrada**0.5)/(2*a)
    print("Las soluciones son:", x1, "y", x2)
