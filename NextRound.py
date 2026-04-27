n,k = map(int,(input().split()))

list1 = list(map(int,(input().split())))
list1.sort(reverse = True) # to make the list in dicident order
count = 0
# count the numbers that are greater than and equal to the index"k" in list1
#print(list1)
if list1[k-1] != 0:
    for i in list1:
        if i >= list1[k-1]:
            count+=1
else:
    count = 0       

print(count)