import random
palabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
def elegir_palabra(palabra):
    return random.choice(palabra)
print("La palabra aleatoria es:",elegir_palabra(palabras))
