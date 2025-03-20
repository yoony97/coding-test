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
    left = 0
    right = len(new) - 1
    while left <= right:
        mid = (left+right)//2
        if x <= new[mid]:
            right = mid - 1
        else:
            left = mid + 1 
    
    return left

def find_max(x):
    left = 0
    right = len(new)- 1
    while left <= right:
        mid = (left+right)//2
        if x < new[mid]:
            right = mid - 1
        else:
            left = mid + 1 
    return right





for x1,x2 in queries:
    left = find_min(x1)
    right = find_max(x2)
    print(right-left + 1)