N, K = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input()))

li.sort()
ans = 0
for i in range(N):
    start = [li[i]]
    for j in range(i+1, N):
        minimum = min(min(start), li[j])
        maximum = max(max(start), li[j])
        if maximum - minimum <= K:
            start.append(li[j])
        else:
            ans = max(ans, len(start))

print(ans)