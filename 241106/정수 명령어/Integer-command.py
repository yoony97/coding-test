from sortedcontainers import SortedSet
import sys

data = sys.stdin.read().strip().split("\n")
T = int(data[0])
data = data[1:]
for _ in range(T):
    s = SortedSet()
    N = int(data[0])
    for i in range(N):
        op, n = data[i+1].split(" ")
        n = int(n)
        if op == "I":
            s.add(n)
        if op == "D":
            if s:
                if n == -1:
                    s.remove(s[0])
                else:
                    s.remove(s[-1])
    if s:
        print(s[-1], s[0])
    else:
        print("EMPTY")

    data = data[N+1:]