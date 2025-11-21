print("Instrucciones:")
print("Crea una contraseña que cumpla los siguientes requisitos:")
print("Ha de tener entre 6 y 8 caracteres de longitud")
print("El primer carácter ha de ser un número entre el 1 y el 5 incluyendolos")
print("El segundo carácter ha de ser una mayúscula")
print("El tercer carácter ha de ser una letra minúscula")
print("El cuarto carácter ha de incluir uno de los siguientes símbolos: @, #, $, %, &, ?")
contraseña = input("Introduce la contraseña: ")
length=len(contraseña)
error=[]
if not (6<=length<=8):
    error.append("Longitud incorrecta")
if length>=1 and not (contraseña[0].isdigit() and 1<=int(contraseña[0])<=5):
    error.append("error en el carácter 1")
if length>=2 and not contraseña[1].isupper():
    error.append("error en el carácter 2")
if length>=3 and not contraseña[2].islower():
    error.append("error en el carácter 3")
if length>=4 and not contraseña[3] in "@#$%&?":
    error.append("error en el carácter 4")
if length>=5 and not (contraseña[4].isdigit() and 1<=int(contraseña[0])<=5):
    error.append("error en el carácter 5")
if length>=6 and not contraseña[5].isupper():
    error.append("error en el carácter 6")
if length>=7 and not contraseña[6].islower():
    error.append("error en el carácter 7")
if length==8 and not contraseña[7] in "@#$%&?":
    error.append("error en el carácter 8")
if error:
    for e in error:
        print(e)
else:
    print("Contraseña válida")


