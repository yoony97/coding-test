N,  M  =  map(int, input().split())
cnts = [0]*N
answer = []
def choose(cur_num,  start, cnts):
    if cur_num == M:
        #단 M개만 1이여야함
        cnt = 0
        for i in range(N):
            if cnts[i] == 1:
                cnt += 1
        if cnt == M:
            print(' '.join([str(i) for i in answer]))
        return
    
    for i in range(start, N+1):
        answer.append(i)
        cnts[i-1] += 1
        choose(cur_num+1, i + 1, cnts)
        cnts[i-1] -= 1
        answer.pop()

choose(0, 1,  cnts)