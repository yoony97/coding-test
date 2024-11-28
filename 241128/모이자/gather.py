n = int(input())
li = list(map(int, input().split()))

ans = float('inf')
for home in range(n):
    current = 0
    for other in range(n):
        current+= abs((home - other))*li[other]
    ans = min(current, ans)

print(ans)