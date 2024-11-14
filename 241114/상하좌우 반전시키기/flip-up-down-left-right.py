import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
li = [list(map(int, i.split())) for i in inputs[1:]]

cnt = 0

for i in range(1, n):
    for j in range(n):
        if li[i-1][j] == 0:
            li[i-1][j] = 1
            li[i][j] = int(not li[i][j])
            
            if 0 <= i+1 < n:
                li[i+1][j] = int(not li[i+1][j])
            if 0 <= j+1 < n:
                li[i][j+1] = int(not li[i][j+1])
            if 0 <= j-1 < n:
                li[i][j-1] = int(not li[i][j-1])

            cnt += 1

if li[-1][-1] == 0:
    cnt = -1

print(cnt)