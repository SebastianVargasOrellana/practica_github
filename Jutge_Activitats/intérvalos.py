def ordenar_intervalos(intervalo):
    intervalo1 = [int(intervalo[0]), int(intervalo[1])]
    intervalo2 = [int(intervalo[2]), int(intervalo[3])]
    return intervalo1, intervalo2
def intersección_intervalos(intervalo1, intervalo2):
    if intervalo1[0] <= intervalo2[0] and intervalo1[1] <= intervalo2[1]:
        print(nombre.strip() for nombre in sorted([intervalo1[1], intervalo2[0]]))
    elif intervalo1[0] >= intervalo2[0] and intervalo1[1] >= intervalo2[1]:
        print(nombre.strip() for nombre in sorted([intervalo2[1], intervalo1[0]]))
    elif intervalo1[0] <= intervalo2[0] and intervalo1[1] >= intervalo2[1]:
        print(nombre.strip() for nombre in sorted([intervalo2[0], intervalo2[1]]))
    elif intervalo1[0] >= intervalo2[0] and intervalo1[1] <= intervalo2[1]:
        print(nombre.strip() for nombre in sorted([intervalo1[0], intervalo1[1]]))
    else:
        print("[]")
def __main__():
    intervalo=input().split()
    intervalo1, intervalo2 = ordenar_intervalos(intervalo)
    intersección_intervalos(intervalo1, intervalo2)
if __name__ == "__main__":
    __main__()

