n, m = map(int, input().split())
li = list(map(int, input().split()))
ans = 0 
while m != 1:
    print(m, end=' ')
    ans += li[m]
    if m%2 == 0:
        m = m//2
    else:
        m = m - 1
print(ans + li[m])