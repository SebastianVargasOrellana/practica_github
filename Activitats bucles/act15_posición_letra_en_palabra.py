p=input("Introduce la palabra secrteta: ")
while True:
    l=input("Introduce la letra que quieres buscar en la palabra secreta")
    e=input("escriba exit para salir")
    x=p.find(l)
    if x:
        print(f"La letra se encuentra en la posición{x} de la palabra secreta")
    elif not x:
        print("Letra no encontrada en la palabra secreta")
    if e==exit:
        return False
    