l1=["a","b","D","x","r","X","3","h","w","2","i"]
p="s"
while p=="s" and p!="n":
    n=input("Introduzca un número que quiera eliminar: ")
    if n.isnumeric() and n in l1:
        l1.remove(n)
        p=input("¿Desea introducir otro número? s/n: ")
    elif n not in l1 or not n.isnumeric():
        print("Introduzca un número que se encuentre en la lista")
        p=input("¿Desea introducir otro número? s/n: ")
print(l1)
