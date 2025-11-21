numero=input("Ingrese un numero entero positivo: ")
palabras= []
while True:
    palabra=input("Ingrese una palabra (o 'FIN' para terminar): ")
    if palabra.upper() == "FIN":
        break
    if len(palabra) == int(numero):
        l=list(palabra)
        for x in l:
            if l.count(palabra)<=1:
                palabras.append(palabra)
for p in palabras:
    print(p)

