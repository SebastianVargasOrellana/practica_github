a=int(input("Introduce el primer intervalo"))
b=int(input("Introduce el segundo intervalo"))
if a<b:
    for i in range (a, b):
        print(end=f'-{i}')
elif b<a:
    for i in range (b, a, -1):
        print(end=f'-{i}')