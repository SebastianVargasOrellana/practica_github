# Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:

palabra=input("Introduce una palabra")
vocales=[]
consonantes=[]
for c in palabra:
    if c in "aeiou":
        c.append(vocales)
    elif c not in "aeiou":
        c.append(consonantes)
print(f'vocales de la palabra{palabra} son: {vocales}')
print(f'consonantes de la palabra{palabra} son: {consonantes}')
