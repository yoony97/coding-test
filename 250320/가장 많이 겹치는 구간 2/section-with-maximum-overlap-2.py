n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

points = []
for s,e in intervals:
    points.append((s,1))
    points.append((e,-1))

points.sort()

max_count = 0
current = 0
for s, v in points:
    current += v
    if max_count < current:
        max_count = current

print(max_count) 

# Please write your code here.
