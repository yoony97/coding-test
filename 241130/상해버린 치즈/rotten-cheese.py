N, M, D, S = map(int, input().split())
history = [] #치즈 먹은 기록
info = [] # 아픈 기록
coodinate = set([i for i in range(1, M+1)])
#상한 치즈를 먹은 최대 사람의 수

for i in range(D):
    p, m, t = map(int, input().split())
    history.append((p,m,t))
    # 사람(p)이 몇 번째 치즈(m)를 언제 먹었는지(t초)
for i in range(S):
    p, t = map(int, input().split())
    info.append((p,t))
    # 사람(p)이 언제 확실히 아팠는지(t초)
# 시간순으로 정렬
info.sort(key = lambda x:x[1])
history.sort(key = lambda x:x[2])


# for i in range(D):
#     p,m,t = history[i]
#     print(f"{p}번 사람이 {m}번 치즈를 {t}초에 먹음")

# 상한 치즈 후보군은 아픈 사람 sp가 st 이전에 먹은 치즈가 후보군이다.
# 이 때, 아픈 사람 A가 먹은 치즈 중 아픈 사람 B가 안먹은 치즈가 존재한다면 제외한다.

for i in range(S):
    sp,st = info[i] #아픈사람 sp, 아픈 시간 st
    eat = set() #아픈 사람이 먹은 치즈 목록
    for j in range(D): #기록 뒤지기
        p, m, t = history[j]
        if sp == p and t < st: #아픈 사람이 아프기 전에 먹은 치즈들
            eat.add(m)
    
    coodinate = coodinate & eat


#i가 상한 치즈일 떄, 몇명이 먹었을까
ans = 0
#print(coodinate) #

for coord in list(coodinate):
    cnt = set()
    for j in range(D):
        p, m, t = history[j]
        if coord == m:
            cnt.add(p)
    ans = max(len(cnt), ans)

print(ans)
