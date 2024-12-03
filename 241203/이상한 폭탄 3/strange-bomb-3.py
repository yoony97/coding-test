N, K = map(int, input().split())
boom = []

cnt = dict()
for i in range(N):
    a = int(input())
    boom.append(a)
    cnt[a] = 0


for i in range(N):
    total = 1
    isboom = False
    for j in range(i+1, N):
        if boom[i] == boom[j]:
            dist = j-i
            if dist <= K:
                total += 1
                isboom = True
    if isboom:
        cnt[boom[i]] = max(total+1, cnt[boom[i]])
    else:
        cnt[boom[i]] = max(0, cnt[boom[i]])

maximum = 0
ans = 0
for i in cnt:
    if maximum < cnt[i]:
        maximum = cnt[i]
        ans = i
    elif maximum == cnt[i] and maximum != 0:
        ans = max(i, ans)

print(ans)