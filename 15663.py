import sys
from itertools import combinations_with_replacement
data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split(" "))
li = list(map(int, data[1].split(" ")))
li.sort()
answer = combinations_with_replacement(li, M)
answer = sorted(set(answer))
for i in answer:
    print(' '.join([str(j) for j in i]))