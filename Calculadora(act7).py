var1=float(input("Introdueix un valor: "))
var2=float(input("Introdueix un altre valor: "))
eleccion=input("Vols sumar, restar, dividir, multiplicar, potenciar, arrel quadrada o residu?(1/2/3/4/5/6/7): ")
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
                    elif eleccion==6:
        print("El total és: ",var1**(1/var2))
                        elif eleccion==6:
        print("El total és: ",var1%var2)

                            print("Operació no vàlida") 