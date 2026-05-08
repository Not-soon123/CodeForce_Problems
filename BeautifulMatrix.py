rows = 5
columens = 5

matrics = []
for row in range(rows):
    row = list(map(int, input().split()))
    matrics.append(row)
#print(matrics[0])

for i in range(rows):
    for j in range(columens):
        if matrics[i][j] == 1:
            row = i + 1
            columen = j + 1
            print(abs(row-3) + abs(columen-3))
            
                