import random
puntuaciones = []
while True:
    lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
    secreta = random.choice(lista)
    intentos = 0
    while True:
        intento = input("Introduce la palabra secreta: ")
        intentos += 1
        if intento == secreta:
            puntos = max(8 - intentos + 1, 1)
            puntuaciones.append(puntos)
            break
    if input("¿Otra partida? s/n: ") == "n":
        break
total = sum(puntuaciones)
media = 8 * len(puntuaciones) / 2
print("Puntuación", puntuaciones)
print("Tu puntuación ha sido de", total)
print("La media las partidas realizadas es:", media)
print("Tienes buena suerte" if total > media else "Dedícate al parchís")