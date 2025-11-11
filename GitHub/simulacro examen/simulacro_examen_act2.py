frase=input("Introduce una frase: ")
frase=frase.lower()
frase=frase.replace(" ","")
num1=float(input("Introduce un numero: "))
num2=float(input("Introduce otro numero: "))
num3=float(input("Introduce un ultimo numero: "))
suma=num1+num2+num3
producto=num1*num2*num3
if num1>=num2 and num1<=num3 or num1<=num2 and num1>=num3:
    media=round(num1,2) 
elif num2>=num1 and num2<=num3 or num2<=num1 and num2>=num3:
    media=round(num2,2)
else:
    media=round(num3,2)
print("La frase en minusculas y sin espacios es: ",frase)
print ("la suma de los numeros es: ",suma)
print("El numero medio es: ",media)
print("El producto de los numeros es: ",producto)



