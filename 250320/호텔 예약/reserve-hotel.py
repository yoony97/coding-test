n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
points = []
for interval in intervals:
    points.append((interval[0],1))
    points.append((interval[1]+1,-1))


points.sort()

max_count = 0
temp =0
for s, v in points:
    temp += v
    max_count = max(max_count, temp)

print(max_count)


