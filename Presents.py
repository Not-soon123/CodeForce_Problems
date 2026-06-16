n = int(input())
friend_who_gives_gift = list(map(int,input().split()))
result = []
for i in range(1,n+1):
    result.append(friend_who_gives_gift.index(i) + 1)
for i in result:
    print(i, end=" ")

