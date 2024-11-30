N, K = map(int, input().split())
position = [0]*(N)
for i in range(N):
    position[i] = int(input())
ans = -1
for i in range(N):
    for j in range(i+1, N):
        if position[i] == position[j] and abs(i-j) <= K:
            ans = max(ans, position[i])

print(ans)