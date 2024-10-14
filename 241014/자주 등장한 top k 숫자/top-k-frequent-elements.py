n, k = map(int, input().split())
li = list(map(int, input().split()))
d = dict()

for i in li:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d = sorted(d, key= lambda x: (d[x],x), reverse= True)
print(' '.join([str(i) for i in d[:k]]))