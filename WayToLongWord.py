number = int(input("Enter the number of words: "))

for i in range(number):
    
    work = input("Enter the word: ")
    workLength = len(work)
    if workLength > 10:
        print(work[0] + str(workLength - 2)+ work[-1] )
    else:
        print(work)


