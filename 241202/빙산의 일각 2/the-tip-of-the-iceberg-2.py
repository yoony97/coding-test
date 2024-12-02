import sys
data = list(map(int, sys.stdin.read().strip().split("\n")))
N = data[0]
H = data[1:]

ans = 0
for th in range(1,1001): #해수면 높이 th
    cnt = 0
    isexist = False
    for i in range(N):
        if H[i] - th > 0 and not isexist:
            cnt += 1
            isexist = True
        elif H[i] - th <= 0 and isexist:
            isexist = False
    ans = max(cnt, ans)

print(ans)