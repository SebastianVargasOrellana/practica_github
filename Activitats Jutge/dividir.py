ln=[]
while len(ln)<2:
    n=input()
    ln.extend(int(i) for i in n.split())
    if len(ln)>=2:
        break
d=ln[0]/ln[1]   
r=ln[0]%ln[1]
print(int(d), r)