l1=["a","b","D","x","r","X","3","h","w","2","i"]
val=len(l1)
n=0
m=0
l=0
lista2=[]
for v in l1:
    if v.isnumeric():
        lista2.append(v)
        n+=1
    elif v.isalpha:
        l+=1
        if v.isupper():
            m+=1
s=sum(list(map(int, lista2)))
print(f"Número de valores: {val}")
print(f"Cantidad de números: {n}")
print(f"Cantidad de letras: {l}")
print(f"Cantidad de mayúsculas: {m}")
print(f"Suma total de números: {s}")