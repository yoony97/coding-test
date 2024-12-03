N, K = map(int, input().split())
rocks = list(map(int, input().split()))
current = 0
ans = float('inf')
paths = []
for i in range(max(rocks), 0, -1):
    path = []
    for idx, rock in enumerate(rocks):
        if rock <= i:
            path.append(idx)
    paths.append(path)

#print(paths)

for path in paths:
    ispossible = True
    if len(path) != 1:
        for i in range(1, len(path)):
            if not(path[i] - path[i-1] <= K):
                ispossible = False
                break
        if ispossible:
            #print(max([rocks[k] for k in path]))
            ans = min(max([rocks[k] for k in path]), ans)

print(ans)