N = int(input())
info = {}
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    if a not in info:
        info[a] = b
    else:
        if info[a] != b:
            ans += 1 

print(ans)

