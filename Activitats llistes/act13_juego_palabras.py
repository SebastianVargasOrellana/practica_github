import random
puntos=[]
partidas_jugadas=0
s_j="s"
while s_j=="s":
    punto=8
    p=""
    palabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
    def elegir_palabra(lista):
        return random.choice(lista)
    palabra_random=elegir_palabra(palabras)
    while p!=palabra_random:
        p=input("Introduce una palabra de la lista: ")
        if p!=palabra_random:
            print("Palabra incorrecta, sigue jugando")
            puntos-=1
    print("Has acertado la palabra")
    puntos.append(punto)
    partidas_jugadas+=1
    s_j=input("Desea seguir jugando? s/n: ")
sp=sum(list(map(int, puntos)))
mp=partidas_jugadas*4
print("Puntuación: ",puntos)
print("La puntuación ha sido de: ",sp)
print("La media de partidas realizadas es: ",mp)
if sp<mp:
    print("Malo")
elif sp>mp:
    print("Bueno")
    