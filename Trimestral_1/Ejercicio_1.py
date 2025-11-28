var_min=input(int("Introduce el número inicial del rango: "))
var_max=input(int("Introduce el número final del rango: "))
var_intervalo=input(int("Introduce el intérvalo entre cada número: "))
for i in range (var_min, var_max, var_intervalo):
    print(i)
    i+=1