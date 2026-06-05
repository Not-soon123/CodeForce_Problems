numMagnet = int(input())
groupCounter = 0
magnetArray = []
for i in range(numMagnet):
    magnet = input()
    magnetArray.append(magnet)
for i in range(1,numMagnet):
    if magnetArray[i] != magnetArray[i-1]:
        groupCounter += 1
print(groupCounter)