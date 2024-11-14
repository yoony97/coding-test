import sys
inputs = sys.stdin.read().strip().split('\n')
n = int(inputs[0])
li = [list(map(int, [k for k in str(i)])) for i in inputs[1:]]

cnt = 0

def change(col, row):
    for i in range(0, col+1):
        for j in range(0, row+1):
            li[i][j] = int(not li[i][j])

for i in range(n-1, -1, -1):
    for j in range(n-1, -1 ,-1):
        if li[i][j] == 1:
            cnt += 1
            change(i,j)

print(cnt)
            
        