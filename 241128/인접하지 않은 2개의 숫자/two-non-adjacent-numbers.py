n = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i+2, N):
        s = li[i] + li[j]
        ans = max(ans, s)

print(ans)
