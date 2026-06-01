numRooms = int(input())
count = 0
for i in range(numRooms):
    pi,qi = map(int, input().split())
    if pi + 2 <= qi:
      count +=  1
    else:
       continue
print(count)
     