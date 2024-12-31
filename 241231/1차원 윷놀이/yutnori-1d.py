N, M, K = map(int, input().split())
paths = list(map(int, input().split()))
answer = 0
coordinate = []

def get_score(coordinate):
    current_point = [0]*K
    scores = 0
    for i in range(N):
        current_point[coordinate[i]] += paths[i]

    for i in range(K):
        if current_point[i] >= M-1:
            scores += 1

    return scores

#리스트에 후보군을 넣는 걸로 하자.

def choose(cur_num):
    global answer

    if cur_num == N:
        answer = max(answer, get_score(coordinate))
        return 
    
    for i in range(K):
        coordinate.append(i)
        choose(cur_num+1)
        coordinate.pop()

choose(0)

print(answer)