#Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
n=int(input("Introduce la cantidad de números que escribirás"))
numero_natural=0
numero_negativo=0
numeros_ceros=0
for x in range (n):
    numero=float(input("Introduce un número"))
    if numero<0:
        numero_negativo+=1
    if numero==0:
        numeros_ceros+=1
    if numero>0:
        numero_natural+=1
print(f'La cantidad de números positivos es {numero_natural}')
print(f'La cantidad de números negativos es {numero_negativo}')
print(f'La cantidad de números ceros es {numeros_ceros}')

