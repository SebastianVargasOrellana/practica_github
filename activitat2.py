var1=float(input("Introdueix un valor: "))
var2=float(input("Introdueix un altre valor: "))
eleccion=int(input("Vols sumar, restar, dividir, multiplicar, potenciar o arrel quadrada?(1/2/3/4/5/6): "))
if eleccion==1:
    print("El total és: ",var1+var2)
    if eleccion==2:
        print("El total és: ",var1-var2)
        if eleccion==3:
        print("El total és: ",var1/var2)
            if eleccion==4:
        print("El total és: ",var1*var2)
                if eleccion==5:
        print("El total és: ",var1**var2)
                    if eleccion==6:
        print("El total és: ",var1**(1/var2))
                        else:
                            print("Operació no vàlida") 