x=int(input())
y=int(input())
lista=[]
for _ in range (y):
    lista.append(".")
for _ in range (x):
    lista.extend(lista)
print (lista)
