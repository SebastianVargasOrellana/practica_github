nombre=input("Introduce tu nombre: ")
nombre=nombre.upper()
edad=int(input("Introduce tu edad: "))
if edad > 0 and edad < 100:
    futuro=2025+(100-edad)
    print("Hola",nombre,"tendrás 100 años en el año",futuro)
else:
    print("Edad no válida")