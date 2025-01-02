N,M = map(int, input().split())
numbers = list(map(int, input().split()))
coord = []
answer = 0

def choose(cur_num, start):
    global answer
    if len(coord) == M:
        temp = coord[0]
        for i in range(1, len(coord)):
            temp ^= coord[i]
        #print(temp, coord)
        answer = max(answer, temp)    
        return

    for i in range(start, N):
        coord.append(numbers[i])
        choose(cur_num+1, i+1)
        coord.pop()
        #choose(cur_num+1, i+1)


choose(0, 0)
print(answer)