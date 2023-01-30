input_coin = int(input('받은금액 : '))

count = 0

coins = [500, 100, 50, 10]

for coin in coins:
   count += input_coin // coin
   print(count)
   input_coin %= coin
# while input_coin >= 500:
#     input_coin -= 500
#     remaining_count += 1
#
# while input_coin >= 100:
#     input_coin -= 100
#     remaining_count += 1
#
# while input_coin >= 50:
#     input_coin -= 50
#     remaining_count += 1
#
# while input_coin >= 10:
#     input_coin -= 10
#     remaining_count += 1

print(input_coin)
print(count)