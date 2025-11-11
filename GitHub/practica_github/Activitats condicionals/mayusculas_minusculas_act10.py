### Ejercicio 10
import string
letra=input("Introduce una letra: ")
mayuscula=letra.isupper()
minuscula=letra.islower()
if mayuscula:
    print("La letra es mayuscula")
elif minuscula:
    print("La letra es minuscula")
elif letra.isdigit():
    print("Es un número")
#añado una condición para saber si el caracter es un caracter especial
elif letra.isalpha and not mayuscula or minuscula():
    print("Es un caracter especial")