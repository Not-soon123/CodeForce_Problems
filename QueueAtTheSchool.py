numQueue, time  = map(int, input().split())
queue = input()
i = 0
for _ in range(time):
    i = 0
    while i < len(queue)-1:
        if queue[i] == 'B' and queue[i+1] == 'G':
            queue = queue[:i] + 'GB' + queue[i+2:]
            i += 1
        i += 1
print(queue)