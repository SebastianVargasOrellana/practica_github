print("***Gasolinera***")
print("1.Sin plomo 95")
print("2.Sin plomo 98")
print("3.Gasoleo A")
print("4.Gasolea A+")
print("*****************")
menu=int(input ( "Introduce una opción: "))
litros=float(input("Introduzca la cantidad de litros a repostar"))
if menu==1:
    precio=round(litros*1.765,2)
    print("El total a pagar es", precio)
elif menu==2:
    precio=litros*1.913
    precio_descuento=precio*0.9
    print("El total a pagar es", precio, "Y con el descuento queda en", precio_descuento)
elif menu==3:
    precio=round(litros*1.746,2)
    print("El total a pagar es", precio)
elif menu==4:
    precio=litros*1.839
    precio_descuento=precio*0.88
    print("El total a pagar es", precio, "Y con el descuento queda en", precio_descuento)

