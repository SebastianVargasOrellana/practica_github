l1=["casa","mesa","sal","sol","agua"]
l2=["casa","luz","tres","tren","sol","pan"]
lr=list(set(l1) & set(l2))
lu=list(set(l1) - set(l2))
lu2=list(set(l2) - set(l1))
print(f"Palabras repetidas: {lr}" "/n" f"Palabras nor repetidas: {lu+lu2}")
