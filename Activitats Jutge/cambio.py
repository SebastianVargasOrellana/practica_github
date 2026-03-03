dinero=input().split()
euros=int(dinero[0])
céntimos=int(dinero[1])
b500=euros//500
b200=euros%500//200
b100=euros%500%200//100
b50=euros%500%200%100//50
b20=euros%500%200%100%50//20
b10=euros%500%200%100%50%20//10
b5=euros%500%200%100%50%20%10//5
m2=euros%500%200%100%50%20%10%5//2
m1=euros%500%200%100%50%20%10%5%2//1
m50=céntimos//50
m20=céntimos%50//20
m10=céntimos%50%20//10
m5=céntimos%50%20%10//5
m2c=céntimos%50%20%10%5//2
m1c=céntimos%50%20%10%5%2//1
print(f"Banknotes of 500 euros: {b500}")
print(f"Banknotes of 200 euros: {b200}")
print(f"Banknotes of 100 euros: {b100}")
print(f"Banknotes of 50 euros: {b50}")
print(f"Banknotes of 20 euros: {b20}")
print(f"Banknotes of 10 euros: {b10}")
print(f"Banknotes of 5 euros: {b5}")
print(f"Coins of 2 euros: {m2}")
print(f"Coins of 1 euro: {m1}")
print(f"Coins of 50 cents: {m50}")
print(f"Coins of 20 cents: {m20}")
print(f"Coins of 10 cents: {m10}")
print(f"Coins of 5 cents: {m5}")
print(f"Coins of 2 cents: {m2c}")
print(f"Coins of 1 cent: {m1c}")