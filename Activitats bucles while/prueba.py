lista=list(input("Introduce números"))
suma=0
target=int(input("Introduce el objetivo de la suma"))  
for i in lista:
    for j in lista:
        if j is i:
            pass
        elif not j is i:
            suma=j+i
        if suma==target:
            break
    if suma==target:
            break
print(f"[{j}, {i}]")