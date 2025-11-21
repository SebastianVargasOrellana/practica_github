tarifa=int(input("1) tarifa nocturna/0.158€ kWh/ 5% de descuento"

           "2) tarifa plna/0.192€ kWh/ 0% de descuento "

           "3) tarifa nocturna/0.143€ kWh/ 8% de descuento"
           
           "4) tarifa nocturna/0.170€ kWh/ 10% de descuento"))
kWh=int(input("introduce los kWh consumidos"))
if tarifa==1:
    precio=kWh*0.158
    descuento=precio*0.05
    total=precio-descuento
    print("el total a pagar es de",precio,"€""Con el descuento aplicado se queda en",total,"€")
elif tarifa==2:
    precio=kWh*0.192
     print("el total a pagar es de",precio,"€""Con el descuento aplicado se queda en",total,"€" )
elif tarifa==3:
    precio=kWh*0.143
    descuento=precio*0.08
    total=precio-descuento
     print("el total a pagar es de",precio,"€""Con el descuento aplicado se queda en",total,"€")
elif tarifa==4:
    precio=kWh* 0.170
    total=precio*0.90
     print("el total a pagar es de",precio,"€""Con el descuento aplicado se queda en",total,"€")
else:
    print("tarifa no valida")
    