s = "pnnepelqomhhheollvlo"
hello = []
for i in s:
    if i == "h" :
        hello.append(i)
        if hello.count(i) > 1:
            hello.pop()
    elif i == "e":
        hello.append(i)
        if hello.count(i) > 1:
            hello.pop()
    elif i == "l" :
        hello.append(i)
        if hello.count(i) > 2:
            hello.pop()
    elif i == "o":
        hello.append(i)
        if hello.count(i) > 1:
            hello.pop()
print(hello)
if hello == ['h', 'e', 'l', 'l', 'o']:
    print("YES")
else:    print("NO")
    