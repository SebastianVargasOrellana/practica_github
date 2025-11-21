#Pedimos el peso y la altura al usuario, calculamos su índice de masa corporal y mostramos si tiene sobrepeso
Peso=float(input("Introduce tu peso en kg: "))
Altura=float(input("Introduce tu altura en metros: "))
IMC=(Peso/(Altura*Altura))
print("Tu índice de masa corporal es:", IMC)
    if IMC>25:
        print("Tienes sobrepeso")