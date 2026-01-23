import random
p=""
palabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
def elegir_palabra(lista):
    return random.choice(lista)
palabra_random=elegir_palabra(palabras)
while p!=palabra_random:
    p=input("Introduce una palabra de la lista: ")
    if p!=palabra_random:
        print("Palabra incorrecta, sigue jugando")
print("Has acertado la palabra")
