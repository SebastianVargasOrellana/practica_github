ln=[]
while len(ln)<3:
    n=input()
    for num in n.split():
        ln.append(float(num))
    if len(ln)>=3:
        break
a= ln.sort(reverse=True)
print(int(ln[0]))