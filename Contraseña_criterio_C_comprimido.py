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
pe=[lambda a: a.isnumeric() and 1<=a<=5, lambda b: b.isupper(), lambda c: c in "* _ @", lambda d: d.isupper(), lambda e: e.isnumeric() and 6<=e<=10,lambda f: f in "& / #", lambda g: g.isnumeric and g<=5 ]
c=input("Introduce una contraseña válida: ")
e=[]
cont=0
x=list(c)
for i, f in enumerate(pe[:len(c)]):
    if not x == pe:
        e.append(i+1)
        cont=cont+1
        print("\n"f"Error en el digito {cont}")
        i+1
if 6>=len(c)<=8:
     print("Contraseña con longitud incorrecta")

    