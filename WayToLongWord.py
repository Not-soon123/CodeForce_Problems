number = int(input())

for i in range(number):
    work = input()
    workLeangth = len(work)
    if workLeangth > 10:
        print(work[0] + str(workLeangth - 2)+ work[-1] )
    else:
        print(work)


