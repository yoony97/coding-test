K, N = map(int, input().split())
answer = []



def choose(cur_num):
    if cur_num == N:
        print(' '.join([str(i) for i in answer]))
        return    

    for i in range(1, K+1):
        if len(answer) >= 2 and answer[-1] == answer[-2] and answer[-1] == i:
            continue
        else:
            answer.append(i)
            choose(cur_num+1)
            answer.pop()

choose(0)