ln=[]
while len(ln)<2:
        n=input()
        ln.extend(n.split())
        if len(ln)>=2:
                break
print(int(ln[0]) + int(ln[1]))