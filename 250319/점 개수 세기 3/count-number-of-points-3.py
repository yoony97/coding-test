

n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]
grid_map = {}
li = [0]*n
psum = [0] *(n+1)

idx = 0
for i in sorted(points):
    grid_map[i] = idx
    li[idx] = 1
    idx += 1


for i in range(n):
    psum[i+1] = psum[i] + li[i]

for s, e in queries:
    rs = grid_map[s]
    re = grid_map[e]+1
    print(psum[re] - psum[rs])