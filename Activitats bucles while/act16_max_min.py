n=0
impar=0
par=0
positivo=0
negativo=0
ceros=0
i=0
lista=[]
while n!=-99:
    n=int(input("Introduce el número que quieras"))
    lista.append(n)
    if int(n)%2==0:
        par+=1
    if int(n)%2!=0:
        impar+=1
    if n<0:
        negativo+=1
    if n>0:
        positivo+=1
    if n==0:
        ceros+=1
    if n==-99:
        negativo-=1
        impar-=1
        i-=1
    i+=1
mayor=max(lista)
menor=min(lista)
print("Resumen")
print(f"El mayor número es: {mayor}")
print(f"El menor número es: {menor}")
print(f"El número de pares es: {par}")
print(f"El número de impares es: {impar}")
print(f"El número de positivos es: {positivo}")
print(f"El número de negativos es: {negativo}")
print(f"El número de ceros es: {ceros}")
print(f"el total es: {i}")