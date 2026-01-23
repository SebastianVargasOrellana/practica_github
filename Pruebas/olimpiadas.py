x=int(input("Introduce las fiulas que quieras"))
y=int(input('Introduce las columnas que quieras'))
cmatriz=[]
matriz=[]
for i in range (y):
    cmatriz.append(".")
for i in range (x):
    matriz.append(cmatriz)
print(*matriz)