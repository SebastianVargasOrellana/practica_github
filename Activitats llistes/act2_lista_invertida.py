#Introducimos una variable que pide el número de elementos en la lista
nel=int(input("Introduce el número de elementos de la lista"))
l=[]
for i in range (nel):
    e=input("Introduce el elemento")
    l.append(e)
lr=l[::-1]
print(l)
print(lr)