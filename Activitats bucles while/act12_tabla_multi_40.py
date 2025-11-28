n=int(input("Introduce el número del que quieras saber su tabla de multipicar"))
i=0
ni=0
while i<10 and ni<=40:
    ni=n*i
    if ni<=40:
        print(ni)
        i+=1