n = int(input())
x = 0

for _ in range(n):
    statement = input().lower()
    if statement == "++x" or statement == "x++":
        x += 1
    else:
        x -= 1
print(x)