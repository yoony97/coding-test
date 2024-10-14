n, k = map(int, input().split())
li = list(map(int, input().split()))
prefix = [0]*(n+1)

for i in range(1, n):
    prefix[i] = prefix[i-1] + li[i]

a = 0
maximum = 0 
for i in range(k, n):
    if maximum < prefix[i] - prefix[a]:
        maximum = prefix[i] - prefix[a]
    a += 1
print(maximum)