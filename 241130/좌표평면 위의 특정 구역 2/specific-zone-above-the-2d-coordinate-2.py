N = int(input())
points = []

def get_box(li):
    min_x = float('inf')
    min_y = float('inf')

    max_x = 0
    max_y = 0
    for i in li:
        min_x = min(i[0],  min_x)
        min_y = min(i[1], min_y)

        max_x = max(i[0], max_x)
        max_y = max(i[1], max_y)

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