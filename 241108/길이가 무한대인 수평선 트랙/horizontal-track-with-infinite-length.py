# A가 달리다 사람 B와 만나게 되면 속력을 줄여 B와 함께 뛰어야하며, A와 B를 하나의 달리기 그룹이 되었다고 표현합니다.
# 총 몇 개의 달리기 그룹이 있는지 구하는 프로그램을 작성해보세요. 
#즉, T분에 같은 위치에 있는 사람들을 한 그룹이라고 하면 총 몇개의 그룹이 생기는지 구해야합니다. 각 그룹은 1명 이상의 사람을 포함합니다.
import sys
from sortedcontainers import SortedSet
inputs = sys.stdin.read().strip().split("\n")
N, T = map(int, inputs[0].split())

s = SortedSet()
for i in range(N):
    l, v = map(int, inputs[i+1].split()) # locate, velocity
    s.add((l,v))

for _ in range(T):
    #print(s)
    for _ in range(len(s)):
        l, v = s.pop(0)
        s.add((l+v, v))
print(len(s))