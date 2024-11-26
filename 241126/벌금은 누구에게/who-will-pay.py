N, M, K = map(int, input().split())
students = [0]*N
ans = -1
for i in range(M):
    idx = int(input()) - 1
    students[idx] += 1
    if students[idx] >= K:
        ans = idx+1
        break

print(ans)