c=int(input("Introduce el número de cifras: "))
nums=input("Introduce los números: ")
suma=0
if len(str(nums))==c:
    for n in nums:
        suma+=int(n)
    print(suma)
elif not len(str(nums))==c:
    print("Error, no coincide el número de cifras")
