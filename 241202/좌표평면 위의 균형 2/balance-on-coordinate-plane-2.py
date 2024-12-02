
N = int(input())
min_M = float('inf')
points  = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x,y))

for lx in range(0,100,2):
    for ly in range(0,100,2):
        p1, p2, p3, p4 = 0, 0, 0, 0
        for point in points:
            x, y = point
            if x > lx and y > ly:
                p1 += 1
            elif x > lx and y < ly:
                p4 += 1
            elif x < lx and y > ly:
                p2 += 1
            else:
                p3 += 1
        M = max(p1,p2,p3,p4)
        min_M = min(M, min_M)

print(min_M)