num_of_coins = int(input())

value_of_coin = list(map(int,(input().split())))
value_of_coin.sort(reverse= True)
minimum_coin = 0
for i in range(num_of_coins+1):
     if sum(value_of_coin[:i]) > sum(value_of_coin[i:]):
          minimum_coin += len(value_of_coin[:i])
          break

print(minimum_coin)
