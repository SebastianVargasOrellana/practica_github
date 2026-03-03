ln=[]
while len(ln)<3:
        n=input()
        ln.extend(n.split())
        if len(ln)>=3:
                break
print(int(ln[0]) + int(ln[1]) + int(ln[2]))