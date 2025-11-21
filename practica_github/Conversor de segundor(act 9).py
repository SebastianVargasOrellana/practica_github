#Pedimos los segundos al usuario y los convertimos a minutos y horas
segundos=int(input("Introdueix els segons a convertir"))
minutos=segundos/60
horas=minutos/60
print(segundos,"segons són",minutos,"minuts o",horas,"hores")