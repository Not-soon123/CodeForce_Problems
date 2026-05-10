numberOfStone = int(input())

QueueOfStones = input()
#print(QueueOfStones[0])

count = 0

i = 0
while i+1 < len(QueueOfStones):
    if QueueOfStones[i] == QueueOfStones[i+1]:
        #print(QueueOfStones[i],QueueOfStones[i+1])
        count += 1
        i += 1
        #print("Inside If : ",i)
    else:
        i += 1
        #print("Inside Else : " , i)
        

print(count)