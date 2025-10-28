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
error=[]
c=input("Introduce una contraseña válida")
x=list(c)
simbolos1="*_@"
simbolos2="&/#"
if 6<= len(c)>=8:
 if not 1<=x[0]<=5:
    error.append("Error en el dígito 1")
 if not x[1].islower():
    error.append("Error en el dígito 2")
 if not x[2].isupper():
    error.append("Error en el dígito 3")
 if simbolos1 !=x[3]:
    error.append("Error en el dígito 4")
 if not x[4].isupper:
    error.append("Error en el dígito 5")
 if not 6<=x[5]<=10:
    error.append("Error en el dígito 6")
 if simbolos2!=x[6]:
    error.append("Error en el dígito 7")
 if x[7]>=5:
    error.append("Error en el dígito 8")
    print(error)
else:
    if not 6<= len(c)>=8:
        print("Longitud incorrecta")
    else:
        print("Contraseña válida")