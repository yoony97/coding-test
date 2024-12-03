N, K = map(int, input().split())
rocks = list(map(int, input().split()))
current = 0
ans = float('inf')

def check(max_val):
    path = []
    for i,  rock in enumerate(rocks):
        if rock <=  max_val:
            path.append(i)
    
    if 0 not in path:
        return False

    for i in range(1, len(path)):
        dist = path[i] - path[i-1]
        if dist > K:
            return False

    return True

for max_val in range(1, max(rocks)+1):
    if check(max_val):
        ans = min(max_val, ans)

print(ans)