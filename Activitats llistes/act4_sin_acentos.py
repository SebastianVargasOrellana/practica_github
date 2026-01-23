import unicodedata
l=[]
p=""
while p!="n":
    e=input("Introduce una letra")
    if e.isalpha():
        l.append(e)
    p=input("¿Quieres repetir?s/n")
sinduplicados=list(set(l))
sinduplicados=unicodedata.normalize('NFD', sinduplicados)
print(sinduplicados)