import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
inputs = list(map(int, inputs[1:]))

ans = 1
cnt = 1
for i in range(1,n):
    if inputs[i-1] == inputs[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)

print(ans)