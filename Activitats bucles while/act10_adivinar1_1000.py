import random
ns=random.randint(1,1000)
n=0
i=0
while ns!=n:
    n=int(input("Introduce un número"))
    if n<ns:
        print(f"El número secreto es mayor a {n}")
    i+=1
    if n>ns:
        print(f"El número secreto es menor a {n}")
    i+=1
print(f"Has acertado el número en {i} intentos")
