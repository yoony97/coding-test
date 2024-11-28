N, S = map(int, input().split())
maps = list(map(int, input().split()))

def csum(i,j):
    result = 0
    for k in range(N):
        if k != i and k !=j:
            result += maps[k]
    return result

diff = float('inf')
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            result = csum(i,j)
            diff = min(diff, abs(result - S))

print(diff)