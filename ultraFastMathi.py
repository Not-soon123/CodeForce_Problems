num1 = input()
num2 = input()
result = []
for i in range(len(num1)):
    if num1[i] == num2[i]:
        result.append("0")
    else :
         result.append("1")
    

print("".join(result))