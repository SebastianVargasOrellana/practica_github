print("Menú")
print("1.Bocadillo de calamares-9€")
print("2.Bocadillo de chistorra-4.5€")
print("3.Bocadillo de jamón-2.5€")
print("Acompañamiento")
print("1.Bocadillo finas-1.5€")
print("2.Bocadillo gruesas-1.75€")
print("3.Bocadillo rústicas-2€")
print("Bebida")
print("1.coca cola-2€")
print("2.acuarius-1.5€")
print("3.agua-1€")
sn=s
precio=0
while sn!="n":
menu=int(input("¿Que vas a comer hoy?"))
acompañamiento=int(input("¿Con que lo acompañarás?"))
bebida=int(input("¿Que te apetece beber?"))
if menu==1:
    precio+=9
if menu==2:
    precio+=9
if menu==3:
    precio+=9
if acompañamiento==1:
    precio+=9
if acompañamiento==2:
    precio+=9
if acompañamiento==3:
    precio+=9
if bebida==1:
    precio+=9
if bebida==2:
    precio+=9
if bebida==3:
    precio+=9
sn=(input("¿Desea hacer otro pedido?"))
pedido_iva=pedido*1.1
pedido5=pedido*0.95
pedido15=pedido*0.85
print(f"El pedido cuesta {pedido}€")
print(f'El total a pagar con iva es {pedido_iva}')
if 30<=pedido_iva>=20:
    print(f'Con el descuento del 5% por pedidos superiores a 20 euros y inferiores a 30 el pedido cuesta: {pedido5}€')
elif pedido_iva>=30:
    print(f'Con el descuento del 15% por pedidos superiores a 30 euros el pedido cuesta: {pedido15}€')