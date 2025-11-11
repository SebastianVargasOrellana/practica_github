### Ejercicio 13
import string
texto="A quien madruga Dios le ayuda."
palabra=input("Introduce una palabra a buscar: ")
#utilizo el método count para contar las veces que aparece la palabra en el texto
#utilizo el método index para saber la posición de la primera aparición de la palabra en el
cantidad=texto.count(palabra)
posicion=texto.index(palabra)
if cantidad>0:
    print("La palabra ",palabra," se encuentra en la posición ",posicion, "y se repite ",cantidad, "veces")  
else:
    print("La palabra no se encuentra en el texto")