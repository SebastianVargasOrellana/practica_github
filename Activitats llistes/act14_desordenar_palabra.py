import random
palabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
def elegir_elemento(lista):
    return random.choice(lista)
def desordenar_palabra(elemento):
    letras=list(elemento)
    random.shuffle(letras)
    return letras
palabra=elegir_elemento(palabras)
print(desordenar_palabra(palabra))
for i in range (3):
    p=input("Introduce la palabra correcta: ")
    if p==palabra:
        break
    elif p!=palabra:
        print("No has acertado, sigue jugando: ")
