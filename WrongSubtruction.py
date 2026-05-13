s,e = [100000000,9]

for i in range(e):
    if s % 10 == 0:
        s /=10
    elif int(s) == 1:
        break
    else:
        s -= 1
print(int(s))