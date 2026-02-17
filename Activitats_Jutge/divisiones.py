ln=[]
while len(ln)<2:
    n=input()
    for i in n.split():
        ln.append(int(i))
d=ln[0]//ln[1]
r=ln[0]%ln[1]
print(int(d), int(r))