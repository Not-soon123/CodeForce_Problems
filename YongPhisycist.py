n = int(input())
x = []
y = []
z = []

for i in range(n):
    X,Y,Z = list(map(int, input().split()))
    x.append(X)
    y.append(Y)
    z.append(Z)

if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
    print("YES")
else:    
    print("NO")

 #   3
#0 2 -2
#1 -1 3
#-3 0 0
