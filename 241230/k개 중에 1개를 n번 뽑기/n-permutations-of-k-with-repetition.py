K, N = map(int, input().split())
answer = []

def pprint(answer):
    print(' '.join([str(i) for i in answer]))

def choose(cur_num):
    if cur_num == N+1:
        pprint(answer)
        return
    for i in range(1,K+1):
        answer.append(i)
        choose(cur_num+1)
        answer.pop()

choose(1)