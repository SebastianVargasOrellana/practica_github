num1=int(input("Introduce el numero 1"))
num2=int(input("Introduce el otro número"))
if num1<=num2:
    for i in range(num1, num2, 2):
        print(i)
if num1>num2:
    for i in range(num2, num1, 2):
        print(i)