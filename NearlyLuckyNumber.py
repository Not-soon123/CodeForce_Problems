number = "4477909898098"

count = 0

if set(number) == {'4', '7'}:
    print("YES")
else:
    for i in number:
        if i == "4" or i == "7":
            count += 1

    if count == 4 or count == 7:
        print("YES")
    else :
            print("NO")
