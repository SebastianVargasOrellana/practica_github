#Te pide que introduzcas una combinación de 1 y 0
codigo=input("Introduce ceros o unos: ")
c=0
u=0
#Añado una lista para que se introduzca el código codificado según el bucle pasa
codificado=[]
#Analiza todo los dígitos del código
for n in codigo:
    #Si el digito es 0 añade 1 a la variable y si la variable de 1 ya tenia un valor mayor o igual que 2 añade a la lista el número de 1 que habian ej: 1111=41
    if n==0:
        c+=1
        if u>=2:
            codificado.append(f"{u}1")
            u==0
        elif u==1:
            codificado.append("1")
            u==0
    #Si el digito es 1 añade 1 a la variable y si la variable de 0 ya tenia un valor mayor o igual que 2 añade a la lista el número de 0 que habian ej: 0000=40
    elif n==1:
        u+=1
        if c>=2:
            codificado.append(f'{c}0')
            c==0
        elif c==1:
            codificado.append("0")
            c==0
    elif not c==0 or c==1:
        print("No se ha podido codificar")
        break
#Escribe la lista sin los [] gracias al *
print(f"{*codificado}")