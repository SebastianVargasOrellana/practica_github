import random
ns=random.randint(1,5)
n=0
while ns!=n:
    n=int(input("Introduce un número"))
    if 1>n>5 or ns!=n:
        print("No has acertado")
print("Has acertado el número")
