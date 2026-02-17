p=""
lni=[]
lnc=[]
lnca=[]
while p!='n':
    e=input("Introduce el nombre del estudiante: ")
    ni=input("Introduce la nota de inglés: ")
    nc=input("Introduce la nota de castellano: ")
    nca=input("Introduce la nota de catalán")
    lni.append(ni)
    lnc.append(nc)
    lnca.append(nca)
    p=input("Desea introducir otro estudiante?")
def ordenar_notas(notas):
    lista_ordenada=notas.sort()
    return lista_ordenada
def mediana_notas(notas):
    m=int(len(notas)//2)
    elemento1=notas[m]
    elemento2=notas[m-1]
    if int(m)%2==0:
        mediana=elemento1+(elemento2-elemento1)/2
    elif int(m)%2!=0:
        mediana=int(m)
    return mediana
def media_notas(notas):
    d=len(notas)
    media=sum(map(int, notas))/d
    return media
print("Inglés: ",ordenar_notas(lni))
print("Castellano: ",ordenar_notas(lnc))
print("Catalán: ",ordenar_notas(lnca))
print("La media de inglés es: ",media_notas(lni))
print("La media de castellano es: ",media_notas(lnc))
print("La media de catalán es: ",media_notas(lnca))
print("La mediana de inglés es: ",mediana_notas(lni))
print("La mediana de castellano es: ",mediana_notas(lnc))
print("La mediana de catalán es: ",mediana_notas(lnca))