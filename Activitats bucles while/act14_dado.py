import random
v1=0
v2=0
v3=0
v4=0
v5=0
v6=0
for i in range (100):
    n=random.randint(1, 6)
    match n:
        case 1:
            v1+=1
        case 2:
            v2+=1
        case 3:
            v3+=1
        case 4:
            v4+=1
        case 5:
            v5+=1
        case 6:
            v6+=1
print(f"uno: {v1}")
print(f"dos: {v2}")
print(f"tres: {v3}")
print(f"cuatro: {v4}")
print(f"cinco: {v5}")
print(f"seis: {v6}")