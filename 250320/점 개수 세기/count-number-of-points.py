from sortedcontainers import SortedSet
n, q = map(int, input().split())

points =  list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

maps = {}
new = SortedSet()

for i in points:
    new.add(i)

idx = 0
for i in new:
    maps[i] = idx
    idx += 1


def find_min(x):
    for i in range(len(new)):
        if x <= new[i]:
            return i
    #return 0

def find_max(x):
    for i in range(len(new)-1, -1, -1):
        if new[i] <= x :
            return i         
    return len(new)-1




for x1,x2 in queries:
    print(find_max(x2) - find_min(x1) +1)