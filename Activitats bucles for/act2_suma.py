#Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n=int(input("Introduce hasta que número quieres hacer la suma consecutiva"))
num=n
x=0
for i in range (n+1):
    x+=i
print(x)