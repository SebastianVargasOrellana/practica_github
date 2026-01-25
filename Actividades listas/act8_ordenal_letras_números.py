lista = ['a','b','D','x','r','X','3','h','w','2','i']
opcion = int(input("Introduce 1 ascendente o 2 descendente: "))
numeros = sorted([int(x) for x in lista if x.isdigit()], reverse=opcion==2)
letras = sorted([x for x in lista if x.isalpha()], key=str.lower, reverse=opcion==2)
print(numeros)
print(letras)