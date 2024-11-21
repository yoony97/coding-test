n, m = map(int, input().split())
li = list(map(int, input().split()))
ans = 0
for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum(li[a1-1:a2]))
