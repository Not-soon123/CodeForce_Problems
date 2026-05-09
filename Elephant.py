LocationOfFriend = int(input())
stepAtOnce = [1,2,3,4,5]
step = 0
if 1 < LocationOfFriend < 1000000:
    i = 4
    while LocationOfFriend >= stepAtOnce[i]:
          LocationOfFriend -= stepAtOnce[i]
          step += 1

          if LocationOfFriend < stepAtOnce[i]:
               while LocationOfFriend <= stepAtOnce[i]:
                     i -= 1
print(step)
               

