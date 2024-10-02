import sys
from itertools import permutations

data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split(" "))
li = list(map(int, data[1].split(" ")))
answer = permutations(li, M)
answer = sorted(answer)
for i in answer:
    print(' '.join([str(j) for j in i]))