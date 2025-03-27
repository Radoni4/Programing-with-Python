days = int(input())
confectioner = int(input())
cakes = int(input())
gofreti = int(input())
puncakes = int(input())

price_cakes = cakes * 45
price_gofreti = gofreti * 5.80
price_puncakes = puncakes * 3.20
money_per_day =(price_cakes + price_gofreti + price_puncakes) * confectioner
all_money = money_per_day * days
money_after_spendings = all_money - all_money * 12.5 / 100
print (money_after_spendings)

# Сума след покриване на разходите: 157356.8- 1/8 от 157356.8 = 137687.2лв