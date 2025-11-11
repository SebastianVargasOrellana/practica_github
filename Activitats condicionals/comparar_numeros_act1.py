## Ejercicio 1
valor1=float(input("Introduce el primer valor: "))
valor2=float(input("Introduce el segundo valor: "))
#realizo las comparaciones con el condicional if, elif y else
if valor2>valor1:
    print(valor1, "es menor que" ,valor2)
elif valor2<valor1:
    print(valor1, "es mayor que" ,valor2)
elif valor2==valor1:
    print(valor1, "es igual que" ,valor2)