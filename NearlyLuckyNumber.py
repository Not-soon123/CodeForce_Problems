number = input()

count = 0

for i in number:
    if i == "4" or i == "7":
        count += 1

if set(str(count)) <= {'4', '7'} and count != 0:
    print("YES")
else:
    print("NO")