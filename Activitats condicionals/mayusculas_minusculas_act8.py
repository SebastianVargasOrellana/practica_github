### Ejercicio 8
#realizo la importación de la librería string
import string
letra=input("Introduce una letra: ")
#utilizo los métodos isupper e islower para determinar si la letra es mayuscula o minuscula
mayuscula=letra.isupper()
minuscula=letra.islower()
if mayuscula:
    print("La letra es mayuscula")
elif minuscula:
    print("La letra es minuscula")