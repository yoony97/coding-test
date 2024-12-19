n, t = map(int, input().split())
maps = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

maps.extend(b)
maps.extend(a)
#print(maps)
#maps = maps[::-1]

for _ in range(t):
    temp = maps[2*n-1]
    for i in range(2*n-1, 0, -1):
        maps[i] = maps[i-1]
    maps[0] = temp 

a = maps[:n]
b = maps[n:]
print(' '.join([str(i) for i in b]))
print(' '.join([str(i) for i in a]))