luky_numbers = ["4","7","47","74","444",
                "447","477","474","744",
                "774","747","777"]
test_number = int(input())

almost_luky_number = False
for i in luky_numbers:
    if test_number % int(i) == 0:
        almost_luky_number = True
        break
    else:
        continue

if almost_luky_number:
    print("YES")
else:
    print("NO")
