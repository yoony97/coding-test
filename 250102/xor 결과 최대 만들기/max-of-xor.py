N,M = map(int, input().split())
numbers = list(map(int, input().split()))
coord = []
answer = 0

def choose(cur_num, start):
    global answer
    if cur_num == M:
        temp = coord[0]
        for i in range(1, len(coord)):
            temp ^= coord[i]
        answer = max(answer, temp)
    
    for i in range(start, N):
        coord.append(i)
        choose(cur_num+1, i+1)
        coord.pop()

choose(0, 0)
print(answer)