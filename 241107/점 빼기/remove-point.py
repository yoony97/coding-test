# 각 질의에 대해 주어진 숫자 k보다 x값이 같거나 큰 점 중 x값이 가장 작은 점을 찾아 지우려고 합니다.
# 만약 x값이 가장 작은 점이 여러 개라면, 그 중 y값이 가장 작은 점을 지우면 됩니다.
import sys
from sortedcontainers import SortedSet
inputs = sys.stdin.read().strip().split("\n")

s = SortedSet() #(x,y)
n ,m = map(int, inputs[0].split())

#init s
for i in range(n):
    a, b= map(int, inputs[i+1].split())
    s.add((a,b))
inputs = inputs[n+1:]

#query
for j in range(m):
    idx = s.bisect_left((int(inputs[j]), 1))
    if idx < len(s):
        print(s[idx][0], s[idx][1])
        s.remove(s[idx])
    else:
        print(-1,-1)