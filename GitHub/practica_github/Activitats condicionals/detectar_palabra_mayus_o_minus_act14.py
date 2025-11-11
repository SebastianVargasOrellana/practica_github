## Ejercicio 14
import string
texto="A quien madruga Dios le ayuda."
print(texto)
# paso todo el texto a minusculas para evitar errores de mayusculas o minusculas
texto_minus=texto.lower()
palabra=input("Introduce una palabra a buscar: ")
# paso la palabra a minusculas para evitar errores de mayusculas o minusculas
palabra_minus=palabra.lower()
cantidad=texto_minus.count(palabra_minus)
posicion=texto_minus.index(palabra_minus)
if cantidad>0:
    print("La palabra ",palabra," se encuentra en la posición ",posicion, "y se repite ",cantidad, "veces")  
else:
    print("La palabra no se encuentra en el texto")