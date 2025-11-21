#A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción
palabra=input("Introduce una palabra")
vocales=[]
consonantes=[]
for c in palabra:
    if c in "aeiouAEIOU":
        c.append(vocales)
    elif c not in "aeiouAEIOU":
        c.append(consonantes)
print(f'vocales de la palabra{palabra} son: {vocales}')
print(f'consonantes de la palabra{palabra} son: {consonantes}')