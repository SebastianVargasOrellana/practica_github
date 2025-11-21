# Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
palabra=input("introduce una palabra")
n=0
for c in palabra:
    print(f"En la posición {n} hay una letra {c}")
    n+=1