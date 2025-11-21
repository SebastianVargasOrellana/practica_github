password="a1e4jk"
total_numer=[]
total_vocal=[]
for i in password:
    if  i.isnumeric():
        total_vocal.append(1)
    if i in "aeiouAEIOU":
        total_numer.append(i)
vocales=sum(total_vocal)
numeros=sum(total_numer)
print("Hay {vocales} vocales y {numeros} es la suma de los números")