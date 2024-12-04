N = int(input())
lines = []
for i in range(N):
    x1, x2= map(int, input().split())
    lines.append((x1,x2))

ans = "Yes"
for i in range(N):
    for j in range(N):
        x1, x2 = lines[i]
        x3, x4 = lines[j]
        if x2 < x3 or x4 < x1:
            ans = "No"

print(ans)