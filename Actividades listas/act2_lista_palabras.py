x = int(input("introduce la cantidad de palabras: "))
l1=[]
for i in range(x):
    p=input(f"Introduce {i+1}ª palabra: ")
    l1.append(p)
l1.sort()
l2=l1.copy()
l2.reverse()
print("lista1 contiene: ", l1)
print("lista2: contiene", l2)