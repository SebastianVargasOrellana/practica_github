codigo=int(input("Introduce ceros o unos: "))
c=0
u=0
for n in codigo:
    if n==0 and c:
        c+=1
        if u>=1:
            print(f"{u}1")
            u==0
    elif n==1 and 
        u+=1
        if c>=1:
            print(f'{c}0')
    