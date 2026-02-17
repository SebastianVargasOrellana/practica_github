n=float(input())
if n%1==0:
    n=int(n)
    print(n, n, n)
elif n%1<0.5:
    n=int(n)
    print(n, n+1, n)
else:
    print(int(n), int(n)+1, int(n)+1)
