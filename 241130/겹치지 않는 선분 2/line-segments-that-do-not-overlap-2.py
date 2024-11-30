N = int(input())
lines = []
for i in range(N):
    a, b = map(int, input().split())
    lines.append((a,b))


#겹치지 않는 조건은  (a, 0),(b, 1)의 선분에서 (c, 0), (d,1)일 때
# a > c 일 땐, b < d 면 겹침
# a < c 일 땐, b > d 면 겹침
def check(a,b,c,d):
    if (a > c and b < d)or ( a < c and b > d ):
        return False
    return True

cnt = 0
#겹치는 선분이 있는지 조사할 선분 i
for i in range(N):
    iscrossed = False
    for j in range(N):
        if i == j:
            continue
        a, b = lines[i]
        c, d = lines[j]
        if not check(a, b, c, d): # 겹치니?
            iscrossed = True
            break
    if not iscrossed: #안겹치면 카운팅
        cnt += 1
print(cnt)