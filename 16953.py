import sys
from collections import deque

data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split(" "))
li = deque([(N, 1)])
answer = -1
while li:
    num, c = li.popleft()
    if num == M:
        answer = c
        break
    if num < M:
        li.append((num*2, c+1))
        li.append((int(str(num) + '1'), c+1))

print(answer)
