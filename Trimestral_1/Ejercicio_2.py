suma_p=0
suma_n=0
i=0
while i<6:
    i+=1
    n=int(input("Introduce un número"))
    if n<0:
        suma_n+=n
    elif n>0:
        suma_p+=n
print(f'Suma de números positivos: {suma_p}')
print(f'Suma de números positivos: {suma_n}')
