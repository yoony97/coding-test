n, k = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i,n):
        if li[i] + li[j] == k:
            cnt+=1

print(cnt)