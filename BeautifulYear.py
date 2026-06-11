inputYear = int(input())

while len(str(inputYear)) <= 4:
    inputYear = inputYear + 1
    if len(str(inputYear)) == len(set(str(inputYear))):
        print(inputYear)
        break
    else:
        continue
