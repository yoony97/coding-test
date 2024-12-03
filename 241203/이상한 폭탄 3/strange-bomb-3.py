N, K = map(int, input().split())
boom = []

cnt = dict()
for i in range(N):
    a = int(input())
    boom.append(a)
    cnt[a] = 0


for i in range(N):
    total = 1
    for j in range(i+1, N):
        if boom[i] == boom[j]:
            dist = j-i
            if dist <= K:
                total += 1
    cnt[boom[i]] = max(total, cnt[boom[i]])


print(max([cnt[i] for i in cnt]))
