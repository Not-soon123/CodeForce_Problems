numberOfStone = int(input())

QueueOfStones = input()

count = 0

i = 0
if len(QueueOfStones) == numberOfStone:
    while i+1 < len(QueueOfStones):
        if QueueOfStones[i] == QueueOfStones[i+1]:
            count += 1
            i += 1
        else:
            i += 1
            

    print(count)
else:
    print("Enter the correct number : ")