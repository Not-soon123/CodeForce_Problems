n = int(input())
x = 0
if n >= 1 and n <= 150:
    for _ in range(n):
        statement = input().lower()
        if statement == "++x" or statement == "x++":
            x += 1
        else:
            x -= 1
    print(x)