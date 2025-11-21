#Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre
nombre=input("Introduce tu nombre")
repeticiones=int(input("Introduce las veces que quieres que se repita tu nombre"))
for i in range (int(repeticiones)):
    print(f'{nombre}')