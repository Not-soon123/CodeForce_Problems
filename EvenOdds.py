import math

n,p = map(int,input().split())
odds = math.ceil(n/2)

if p <= odds:
    print(p*2 - 1)
elif p > odds:
     p = p - odds
     print(p*2)

