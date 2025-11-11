## Ejercicio 16
import string
#inicializo valores a cada variable
var_numero="6734"
var_suma=0
#obtengo su longitud
var_longitud = len(var_numero)
#sumo cada digito a partir del índice de cada posición
var_suma =float( var_numero [0] + var_numero [1]+ var_numero[2] + var_numero[3] )
residuo=float(var_suma % 2)
#utilizo una condición y el operador aritmético % para saber si el resto da 0 y ver si es par
if residuo == 0:
    print (f"el valor de {var_suma} es par")