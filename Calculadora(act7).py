var1=float(input("Introdueix un valor: "))
var2=float(input("Introdueix un altre valor: "))
eleccion=input("Vols sumar, restar, dividir, multiplicar, potenciar o arrel quadrada?(s/r/d/m/p/a): ")
if eleccion=="s":
    print("El total és: ",var1+var2)
    elif eleccion=="r":
        print("El total és: ",var1-var2)
        elif eleccion=="d":
        print("El total és: ",var1/var2)
            elif eleccion=="m":
        print("El total és: ",var1*var2)
                elif eleccion=="p":
        print("El total és: ",var1**var2)
                    elif eleccion=="a":
        print("El total és: ",var1**(1/var2))
                        else:
                            print("Operació no vàlida") 