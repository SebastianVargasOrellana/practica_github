### Ejercicio 12
import string
texto=input("Introduce un texto: ")
longitud=len(texto)
if longitud<11:
print("El texto tiene menos de 11 caracteres")
elif longitud>11:
    print("El texto tiene mas de 11 caracteres")
elif longitud==11:
    print("el texto tiene 11 caracteres")