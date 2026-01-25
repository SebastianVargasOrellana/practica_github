lista1 = ["casa","mesa","sal","sol","agua"]
lista2 = ["casa","luz","tres","tren","sol","pan"]

todas = set(lista1 + lista2)
repetidas = list(set(lista1) & set(lista2))
no_repetidas = list(todas - set(repetidas))

print("Están repetidas: ", repetidas)
print("No están repetidas: ", no_repetidas)