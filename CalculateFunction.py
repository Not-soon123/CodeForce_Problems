num = int(input())
count = 0
for i in range(1, num+1):
    print(i)
    if i % 2 == 0:
        count += i
    elif i % 2 != 0:
        count -= i

print(count)