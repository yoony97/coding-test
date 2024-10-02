import sys
from itertools import combinations_with_replacement

data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split(" "))
li = [i for i in range(1,N+1)]
answer = combinations_with_replacement(li, M)
for i in answer:
    print(' '.join([str(j) for j in i]))