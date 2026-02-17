import statistics
ingles, castellano, catalan = [], [], []
while True:
    nombre = input("Introduce estudiante: ")
    ingles.append(float(input("Nota inglés: ")))
    castellano.append(float(input("Nota castellano: ")))
    catalan.append(float(input("Nota catalán: ")))
    if input("Deseas introducir otro alumno s/n: ") == "n":
        break
print("La media en inglés es:", statistics.mean(ingles))
print("La media en castellano es:", statistics.mean(castellano))
print("La media en catalán es:", statistics.mean(catalan))
print("La mediana en inglés es:", statistics.median(ingles))
print("La mediana en castellano es:", statistics.median(castellano))
print("La mediana en catalán es:", statistics.median(catalan))