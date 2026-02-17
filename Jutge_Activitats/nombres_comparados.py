nom=input()
nom=nom.split()
if nom[0]>nom[1]:
    print(nom[0], ">", nom[1])
elif nom[0]<nom[1]:
    print(nom[0], "<", nom[1])
elif nom[0]==nom[1]:
    print(nom[0], "=", nom[1])