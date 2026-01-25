lista = []
while True:
    letra = input("Introduce una letra: ")
    if letra not in lista:
        lista.append(letra)

    repetir = input("¿Deseas repetir s/n: ")
    if repetir.lower() == "n":
        break
print(lista)
