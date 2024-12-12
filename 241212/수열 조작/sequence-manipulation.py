from collections import deque
N = int(input())
li = deque(list(range(1,N+1)))
while len(li) > 1:
    li.popleft() 
    a = li.popleft()
    li.append(a)

print(li[0])