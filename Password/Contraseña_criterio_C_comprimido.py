print("INSTRUCCIONES")
print("La contraseña ha de tener entre 6 y 8 caracteres")
print("Posición 1: El número tiene que ser mayor o igual que 1 y menior o igual que 5")
print("Posición 2: Tiene que ser una minúscula")
print("Posició 3: Tiene que ser una mayúsucla")
print("Posición 4: Tiene que ser uno de los siguientes símbolos: *,_,@")
print("Posición 5: Una letra mayúscula")
print("Posición 6: Un número mayor o igual que 6 y menor o igual que 9")
print("Posició 7: Ha de ser un dels següents símbols: &, /, #")
print("Posició 8: Un número menor o igual que 5")
#Aquí he hecho una lista con los errores definidos con la función lambda
pe = [
    lambda a: a.isnumeric() and 1 <= int(a) <= 5,
    lambda b: b.islower(),
    lambda d: d.isupper(),
    lambda c: c in "* _ @",
    lambda e: e.isnumeric() and 6 <= int(e) <= 10,
    lambda f: f in "& / #",
    lambda g: g.isnumeric() and int(g) <= 5
]

c = input("Introduce una contraseña válida: ")
x = list(c)
e = []

if not 6 <= len(c) <= 8:
    print("Contraseña con longitud incorrecta")
#Aquí he hecho un bucle en el que se compara la lista y la contraseña
for i, (car, regla) in enumerate(zip(x, pe)):
    #Se añade un error a la lista si no son iguales
    if not regla(car):
        e.append((i, car))
#Hago un bucle que escriba los errores en las posiciones de la lista e
for idx, m in e:
    print(f"Error en la posición {idx+1}")
    