n = int(input())
count = 0
for i in range(n):
    v,p,n = map(int, input().split())
    if v+p+n >= 2:
        count += 1
print(count)
   