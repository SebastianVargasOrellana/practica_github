milista=[1,1,2,3,2,1,6,7,1]
for i in milista:
    n=milista.count(i)
    if n>1:
        milista.remove(i)
print(milista)