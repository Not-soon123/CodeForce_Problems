LocationOfFriend = int(input())
stepAtOnce = [1,2,3,4,5]
step = 0
if 1 <= LocationOfFriend <= 1000000:
    while LocationOfFriend > 0:

            if LocationOfFriend >= stepAtOnce[4]:
                  LocationOfFriend -= stepAtOnce[4]
                  step += 1

            elif LocationOfFriend >= stepAtOnce[3]:
                  LocationOfFriend -= stepAtOnce[3]
                  step += 1
                  
            elif LocationOfFriend >= stepAtOnce[2]:
                  LocationOfFriend -= stepAtOnce[2]
                  step += 1

            elif LocationOfFriend >= stepAtOnce[1]:
                  LocationOfFriend -= stepAtOnce[1]
                  step += 1

            else :
                  LocationOfFriend -= stepAtOnce[0]
                  step += 1
                  
            
    print(step)
               

