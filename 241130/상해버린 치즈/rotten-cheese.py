N, M, D, S = map(int, input().split())
history = [] #치즈 먹은 기록
info = [] # 아픈 기록
cheese = set([i for i in range(1, M+1)])
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

# #후보군 찾기
coodinate = set()
for i in range(S):
    sp,st = info[i]
    #st 기분으로 후보군 찾아보기
    #st 보다 작은
    eat = set() 
    for j in range(D):
        p, m, t = history[j]
        if sp == p and t+1 <= st:
            coodinate.add(m)
            eat.add(m)
    #안먹은 치즈
    noteat = cheese - eat
    #안먹은 치즈가 후보군에 포함될 순 없음
    coodinate = coodinate - noteat
#i가 상한 치즈일 떄, 몇명이 먹었을까
ans = 0
print(coodinate)
for coord in list(coodinate):
    cnt = set()
    for j in range(D):
        p, m, t = history[j]
        if coord == m:
            cnt.append(p)
    ans = max(len(cnt), ans)

print(ans)

#1번치즈가 상했을 경우, 1번 사람이 3초에 아프니까 가능
#1