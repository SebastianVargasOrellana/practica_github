print("Instrucciones:")
print("Crea una contraseña que cumpla los siguientes requisitos:")
print("Ha de tener entre 6 y 8 caracteres de longitud")
print("El primer carácter ha de ser un número entre el 1 y el 5 incluyendolos")
print("El segundo carácter ha de ser una minúscula")
print("El tercer carácter ha de ser una letra mayúscula")
print("El cuarto carácter ha de incluir uno de los siguientes símbolos: *,_,@")
print("El quinto carácter ha de ser un número entre el 6 y el 9 incluyendolos")
print("El sexto carácter ha de ser una letra mayúscula")   
print("El séptimo carácter ha de incluir uno de los siguientes símbolos: &,/,#")
print("El octavo carácter ha de ser un número menor o igual a 5")
contraseña = input("Introduce la contraseña: ")
l=len(contraseña)
e=[]
reglas=[(lambda c: c.isdigit() and 1<=int(c)<=5 , 0, "1"), (str.islower, 1, "2"), (str.isupper, 2, "3"), (lambda c: c in "*_@", 3, "4"), (str.islower, 4, "5"), (lambda c: c.isdigit() and 6<=int(c)<=9, 5, "6"), (lambda c: c in "$/#", 6, "7"), (lambda c: c.isdigit() and int(c)<=5, 7, "8")]
for func, pos, carácter in reglas:
    if pos<l and not func(contraseña[pos]):
     e.append(carácter) 
if not (6<=l<=8):
     print("Longitud incorrecta") 
if e:
    for i in e:
     print(f"dígito {i} incorrecto")   
else:
     print("Contraseña válida")


    