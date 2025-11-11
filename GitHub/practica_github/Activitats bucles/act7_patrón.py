n=5
num=[]
for i in range(5):
    for i in range (n, 0, -1):
        num.append(i)
    print(*num)
    num=[]
    n-=1