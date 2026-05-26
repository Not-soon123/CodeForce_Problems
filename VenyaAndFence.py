s,w = [6,5]
a = [7, 6, 8, 9, 10, 5]
count = 0

for i in a:
    if i<=w:
        count +=1
    else:
         count += 2
print(count)
