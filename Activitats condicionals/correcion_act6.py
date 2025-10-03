var1=float(input("Introduce el peso en kg: "))
var2=float(input("Introduce la altura en m: "))
imc=var1 / var2 ** 2
print("Si pesas",var1," kilos y mides ", var2, "tu IMC es:", 
imc)
if imc>25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")