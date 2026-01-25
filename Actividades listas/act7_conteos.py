lista1=['a','b','D','x','r','X','3','h','w','2','i']
numeros=0
letras=0
mayusculas=0
suma=0
for i in lista1:
    if i.isdigit():
        numeros+=1
        suma+=int(i)
    elif i.isalpha():
        letras+=1
        if i.isupper():
            mayusculas+=1
print("Número de valores:", len(lista1))
print("Cantidad de números:", numeros)
print("Cantidad de letras:", letras)
print("Cantidad de mayúsculas:", mayusculas)
print("Suma total de números:", suma)