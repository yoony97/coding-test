N = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(N-2):
    for j in range(i+2, N):
        s = li[i] + li[j]
        ans = max(ans, s)

print(ans)
