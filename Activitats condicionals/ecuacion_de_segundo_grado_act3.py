a=float(input("Introduce el valor de a:"))
b=float(input("Introduce el valor de b:"))
c=float(input("Introduce el valor de c:"))
raizcuadrada=b**2-4*a*c
if raizcuadrada<0:
    print("La ecuacion no tiene solucion en los reales")
elif raizcuadrada>0:
    raizcuadrada=b**2-4*a*c
    x1=(-b+raizcuadrada**0.5)/(2*a)
    x2=(-b-raizcuadrada**0.5)/(2*a)
    print("Las soluciones son:", x1, "y", x2)
