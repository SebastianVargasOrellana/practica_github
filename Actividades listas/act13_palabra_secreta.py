import random
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
secreta = random.choice(lista)
while True:
    intento = input("Introduce la palabra secreta: ")
    if intento == secreta:
        print("ACERTASTE")
        break
    else:
        print("SIGUE JUGANDO")