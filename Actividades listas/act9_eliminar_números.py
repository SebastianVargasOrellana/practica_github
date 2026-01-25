lista = ['a','b','D','x','r','X','3','h','w','2','i']

while True:
    valor = input("Introduce el valor que deseas eliminar: ")

    if not valor.isdigit():
        print("Introduce valor numérico")
    elif valor in lista:
        lista.remove(valor)
        print(lista)
    else:
        print("El valor introducido no está en la lista")

    repetir = input("Deseas introducir otro valor s/n: ")
    if repetir.lower() == "n":
        break