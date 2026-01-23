l=[]
p=""
while p!="n":
    e=input("Introduce una letra")
    if e.isalpha():
        l.append(e)
    p=input("¿Quieres repetir?s/n")
sinduplicados=[]
sinduplicados=list(set(l))
print(sinduplicados)