### Ejercicio 9
letra=input("Introduce una letra: ")
mayuscula=letra.isupper()
minuscula=letra.islower()
if mayuscula:
    print("La letra es mayuscula")
elif minuscula:
    print("La letra es minuscula")
elif letra.isnumeric():
    print("Es un número")