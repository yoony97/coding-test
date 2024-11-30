N = int(input())
points = []

def get_box(li):
    p1, p2, p3 = li
    
    min_x = min(p1[0], p2[0], p3[0])
    min_y = min(p1[1], p2[1], p3[1])

    max_x = max(p1[0], p2[0], p3[0])
    max_y = max(p1[1], p2[1], p3[1])

    return (max_x - min_x)*(max_y - min_y)


for i in range(N):
    a, b = map(int, input().split())
    points.append((a,b))

ans = float('inf')
for i in range(N):
    #제외할 점 i
    p = []
    for j in range(N):
        if i == j:
            continue
        p.append(points[j])
    area = get_box(p)
    ans = min(area, ans)
print(ans)