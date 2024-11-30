N, M, D, S = map(int, input().split())
history = [] #치즈 먹은 기록
info = [] # 아픈 기록

#상한 치즈를 먹은 최대 사람의 수

for i in range(D):
    p, m, t = map(int, input().split())
    history.append((p,m,t))
    # 사람(p)이 몇 번째 치즈(m)를 언제 먹었는지(t초)
for i in range(S):
    p, t = map(int, input().split())
    info.append((p,t))
    # 사람(p)이 언제 확실히 아팠는지(t초)


# for i in range(D):
#     p,m,t = history[i]
#     print(f"{p}번 사람이 {m}번 치즈를 {t}초에 먹음")

#후보군 찾기
coodinate = set()
for i in range(S):
    sp,st = info[i]
    for j in range(D):
        p, m, t = history[j]
        if sp == p and t < st:
            coodinate.add(m)

#i가 상한 치즈일 떄, 몇명이 먹었을까
ans = 0
for coord in list(coodinate):
    cnt = 0
    for j in range(D):
        p, m, t = history[j]
        if coord == m:
            cnt += 1
    ans = max(cnt, ans)

print(ans)