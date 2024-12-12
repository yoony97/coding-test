from collections import deque

n = int(input())
s = deque([])
for i in range(n):
    ops = input().split()
    if ops[0] ==  'push_front':
        s.appendleft(int(ops[1]))
    if ops[0] ==  'push_back':
        s.append(int(ops[1]))

    if ops[0] ==  'size':
        print(len(s))

    if ops[0] ==  'empty':
        if len(s) == 0 :
            print(1)
        else:
            print(0)
    if ops[0] == 'pop_front':
        print(s.popleft())
    
    if ops[0] == 'pop_back':
        print(s.pop())

    if ops[0] == 'front':
        print(s[0])

    if ops[0] == 'back':
        print(s[-1])