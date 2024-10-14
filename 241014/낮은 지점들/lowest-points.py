# dic[x] = y
n = int(input())
d = {}
for i in range(n):
    x,y = map(int, input().split())
    if x in d:
        if y < d[x]:
            d[x] = y
    else:
        d[x] = y


print(sum(d.values()))