n_notas=int(input("Introduce cuantas notas quieres comprobar"))
aprobado=[]
suspenso=[]
for i in range (int(n_notas)):
    nota=float(input("Introduce la nota"))
    if 0<=nota<=10:
        if nota<=4.9:
            aprobado.append(nota)
        elif nota>=5:
            suspenso.append(nota)
    else:
        print('nota fuera del rango')
for nota in aprobado:
    print(f'Has aprobado con un {nota}')
for nota in suspenso:
    print(f'Has suspendido con un {nota}')