N = int(input())
points = []
for i in range(N):
    a, b = map(int, input().split())
    points.append((a,b))

def dist(a,b):
    return (a[0] - b[0])**2+  (a[1] - b[1]) ** 2

ans = float('inf')
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans = min(ans, dist(points[i], points[j]))

print(ans)