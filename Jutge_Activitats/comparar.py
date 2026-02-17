ln=[]
while len(ln)<2:
    n=input()
    ln.extend(n.split())
    if len(ln)>=2:
        break
if float(ln[0])==float(ln[1]):
    print(int(ln[1]))
if float(ln[0])>float(ln[1]):
    print(int(ln[0]))
if float(ln[0])<float(ln[1]):
    print(int(ln[1]))