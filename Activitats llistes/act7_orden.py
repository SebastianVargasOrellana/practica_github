l1=["a","b","D","x","r","X","3","h","w","2","i"]
l2=[]
p=input("Introduce 1 para visualizar en orden ascendente o 2 descendente: ")
for v in l1:
    if v.isnumeric():
        i=l1.index(v)
        n=l1.pop(i)
        l2.append(n)
if p=="1":
    l1.sort(key=lambda v: v.islower())
    l2.sort(key=lambda v: v.islower())
elif p=="2":
    l1.sort(key=lambda v: v.islower(), reverse=True)
    l2.sort(key=lambda v: v.islower(), reverse=True)
print(l1, l2)