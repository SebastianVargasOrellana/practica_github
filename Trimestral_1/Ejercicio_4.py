var_total=50
n=1
while var_total<60 and n!=0:
    n=int(input("Introduce un número"))
    if n%2==0:
        var_total+=n
    if n%2!=0:
        var_total-=n
    print(var_total)
