#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b
a=int(input("Introduce el primer intervalo"))
b=int(input("Introduce el segundo intervalo"))
if a<b:
    for i in range (a, b):
        print(end=f'-{i}')
elif b<a:
    for i in range (b, a, -1):
        print(end=f'-{i}')