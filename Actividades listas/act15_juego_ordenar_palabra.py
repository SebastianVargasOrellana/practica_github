import random
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra = random.choice(lista)
letras = list(palabra)
random.shuffle(letras)
print(letras)
for i in range(3):
    intento = input("Introduce palabra correcta: ")
    if intento == palabra:
        print("Acertaste")
        break
    else:
        print("no has acertado")
else:
    print("no has acertado ninguno de los intentos")