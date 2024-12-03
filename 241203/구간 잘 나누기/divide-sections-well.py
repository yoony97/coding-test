N, M = map(int, input().split())
li = list(map(int, input().split()))

#정답이 될지 안될지 가정해봐야하나??
for i in range(min(li), sum(li)+1):
    #i가 정답일 때:
    m = 0 # 격자 개수
    s = 0 # 격자 안에 있는 수의 합
    for a in range(N):
        if i < s + li[a]: #우리가 정한 정답 보다 합이 클 때
            m += 1
            s = li[a]
        else:
            s += li[a]
    
    if m <= M-1:
        print(i)
        break

    