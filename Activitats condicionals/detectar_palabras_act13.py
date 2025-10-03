import string
texto="A quien madruga Dios le ayuda."
palabra=input("Introduce una palabra a buscar: ")
cantidad=texto.count(palabra)
posicion=texto.index(palabra)
if cantidad>0:
    print("La palabra ",palabra," se encuentra en la posición ",posicion, "y se repite ",cantidad, "veces")  