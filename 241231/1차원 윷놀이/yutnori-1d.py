N, M, K = map(int, input().split())
paths = list(map(int, input().split()))
answer = 0
coordinate = [0]*K

def get_score():
    score = 0
    for i in range(K):
        if coordinate[i] >= M-1:
            score += 1

    return score 

def choose(cur_num):
    global answer
    
    answer = max(answer, get_score())
    
    if cur_num == N:
        return 
    
    for i in range(K):
        if coordinate[i] >= M-1:
            continue
        
        coordinate[i] += paths[cur_num]
        choose(cur_num+1)
        coordinate[i] -= paths[cur_num]

choose(0)
print(answer)