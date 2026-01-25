cantidad = int(input("Introduce la cantidad de números: "))
lista = []

for i in range(cantidad):
    num = int(input("Introduce un número: "))
    lista.append(num)

lista.sort()
print(lista)
