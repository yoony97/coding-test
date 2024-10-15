N = int(input())
li = list(map(int, input().split()))


s = li[0]
maximum = 0
for i in range(1,N):
    if s + li[i] <= li[i]:
        s = li[i]
    else:
        s += li[i]
    maximum = max(s, maximum)
print(maximum)