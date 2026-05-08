wOfBob ,wOfLamek= map(int,input().split())
year = 0
if 1 <= wOfBob <= wOfLamek <= 10:
    while wOfBob <= wOfLamek:
        wOfLamek = wOfLamek * 2
        wOfBob = wOfBob * 3
        year += 1
    print(year)
else:
    print("Invalid weight")
    


