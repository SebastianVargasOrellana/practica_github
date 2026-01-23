w=0
while w==0:
    n=list(input("Introduzca un número"))
    c=0
    d=0
    l=0
    for e in n:
        if e==".":
            c+=1
        if c==1 and e.isnumeric:
            d+=1
        if e.isalpha():
            l+=1
    if l==0:
        if d>=1:
            print("El número introducido es decimal")
        elif d!=1:
            print("El número introducido no es decimal")
        w+=1
    else:
        print("El número no es válido, pruebe otro: ")