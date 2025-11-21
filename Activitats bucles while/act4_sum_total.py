p="s"
sum=0
rep=0
while p!="n":
    num1=float(input("Introduce un número"))
    num2=float(input("Introduce otro número"))
    suma=num1 + num2
    print(suma)
    sum+=suma
    rep+=1
    p=input("¿Quieres seguir calculando? s/n")
print(f"Has hecho {rep} repeticiones y la suma total es {sum}")