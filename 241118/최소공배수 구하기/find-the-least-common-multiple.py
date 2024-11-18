n, m = map(int, input().split())

mi = min(n,m)
for i in range(1, 10000000):
    temp = mi*i
    if temp%n == 0 and temp%m == 0:
        print(temp)
        break
    