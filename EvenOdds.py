n,p = map(int,input().split())
even = []
odd = []
for i in range(1,n+1):
     if i%2 == 0:
         even.append(i)
     else:
          odd.append(i)
        
all = odd + even
print(all[p-1])