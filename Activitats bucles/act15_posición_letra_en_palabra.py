#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
p=input("Introduce la palabra secrteta: ")
for i in range(len(p)):
    l=input("Introduce la letra que quieres buscar en la palabra secreta")
    x=p.find(l)
    if x:
        print(f"La letra se encuentra en la posición{x} de la palabra secreta")
    elif not x:
        print("Letra no encontrada en la palabra secreta")

    