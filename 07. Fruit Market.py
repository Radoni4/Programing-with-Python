strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())
raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (0.4 * raspberries_price)
bananas_price = raspberries_price - (0.8 * raspberries_price)
sum_bananas = bananas * bananas_price
sum_oranges = oranges * oranges_price
sum_raspberries = raspberries * raspberries_price
sum_strawberries = strawberries * strawberries_price
all_sum = sum_bananas + sum_oranges + sum_raspberries + sum_strawberries
print (all_sum)
