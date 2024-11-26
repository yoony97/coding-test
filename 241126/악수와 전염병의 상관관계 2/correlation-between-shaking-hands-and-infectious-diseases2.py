import sys
inputs = sys.stdin.read().strip().split('\n')
N, K, P, T = map(int, inputs[0].split())
inputs = [tuple(map(int, i.split())) for i in inputs[1:]]
inputs.sort(key = lambda x: x[0])

init_value = [0]*(N+1)
init_value[P] = 1

MAX_LEN = 250*250
li = [init_value for _ in range(MAX_LEN)]
counts = [K]*(N+1)
current_t = inputs[0][0]
for i in inputs:
    t, x, y = i
    for m in range(current_t, t):
        li[m] = li[current_t]

    if li[t][x] == 1 and counts[x] > 0:
        li[t][y] = 1
        counts[x] -= 1
    
    if li[t][y] == 1 and counts[y] > 0:
        li[t][x] = 1
        counts[y] -= 1
        
    print(t, counts, li[t])

print(''.join([str(i) for i in li[t][1:]]))
