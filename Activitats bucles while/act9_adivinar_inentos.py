import random
ns=random.randint(1,5)
n=0
i=0
while ns!=n and i<3:
    n=int(input("Introduce un número"))
    if 1>n>5 or ns!=n:
        print("No has acertado")
    i+=1
    if i<3:
        print(f"Te quedan {3-i} intentos")
    elif i==3:
        print("Te has quedado sin intentos")
if ns==n:
    print("Has acertado el número")
