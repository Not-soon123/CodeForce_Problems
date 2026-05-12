s = input()

count = 0
for i in s:
    if i == i.upper():
        count += 1
if count > len(s) // 2:
    #print(len(s)//2)
    print(s.upper())
else:    
    print(s.lower())
