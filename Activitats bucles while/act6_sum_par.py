p="s"
sum=0
rep=0
rsum=1
while p!="n" and sum<50:
    print(f"Has hecho {rep} repeticiones y la suma total es {sum}")
    num1=float(input("Introduce un número"))
    num2=float(input("Introduce otro número"))
    suma=num1 + num2
    print(suma)
    sum+=suma
    rep+=1
    rsum=sum%2
    p=input("¿Quieres seguir calculando? s/n")
print(f"Has hecho {rep} repeticiones y la suma total es {sum}")
print("Fin del programa")