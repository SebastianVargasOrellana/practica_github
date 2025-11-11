p=(input("Introduce la palabra secreta"))
for i in range (5, 0, -1):
    print(f"Te quedan {i} intenos")
    letra=(input("Introduce una letra en la palabra secreta: "))
    x=p.find(letra)
    if x:
        print("La letra está en la palabra")
    if not x:
        print("La palabra no se ha encontrado")
        