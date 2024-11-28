N = int(input())
li = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            A1 = li[i]
            A2 = li[j]
            A3 = li[k]
            if A1 <= A2 <= A3:
                cnt += 1

print(cnt)