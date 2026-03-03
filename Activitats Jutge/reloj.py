t=input().split()
h=int(t[0])
m=int(t[1])
s=int(t[2])
s+=1
if s==60:
    s="00"
    m+=1
if m==60:
    m="00"
    h+=1
if h==24:
    h="00"
if int(h)<10 and h!="00":
    h="0"+str(h)
if int(m)<10 and m!="00":
    m="0"+str(m)
if int(s)<10 and s!="00":
    s="0"+str(s)
print(str(h)+":"+str(m)+":"+str(s))