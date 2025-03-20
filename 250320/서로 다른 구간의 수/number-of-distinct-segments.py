n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
points = []
for s, e in intervals:
    points.append((s,+1))
    points.append((e,-1))

points.sort(key=lambda x: x[0])

cnt = 0
current = 0
for s, v in points:
    current += v
    if current == 0:
        cnt += 1

print(cnt)