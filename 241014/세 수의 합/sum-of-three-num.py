n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = dict()

ans = 0
for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

for i in range(n):
    count[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]

        if diff in count:
            ans += count[diff]
        
print(ans)