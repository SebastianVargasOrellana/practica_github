### Ejercicio 2
valor1=float(input("Introduce el primer valor entre el 0 y 10: "))
valor2=float(input("Introduce el segundo valor entre 0 y 10: "))
#realizo las comparaciones con el condicional if, elif y else
if valor2>10 or valor1>10 or valor1<0 or valor2<0:
    print("Los valores no estan entre 0 y 10")
elif valor2>valor1:
    print(valor1, "es menor que" ,valor2)
elif valor2<valor1:
    print(valor1, "es mayor que" ,valor2)
elif valor2==valor1:
    print(valor1, "es igual que" ,valor2)