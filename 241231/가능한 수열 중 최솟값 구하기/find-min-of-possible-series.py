N = int(input())
target = []
answer = None

def check(target):
    #완전 탐색 어떻게 해야할까?
    #1. 1 ~ M 글자까지 선택
    #2. 해당 글자의 길이만큼 중복이 있는지 확인
    length = len(target)
    target = ''.join([str(i) for i in target])
    for start in range(length):
        for end in range(start+1, length):
            s = target[start:end]
            e = target[end:end+len(s)]
            if s == e:
                return False 
    return True 


def solve(cnt):
    global answer

    if len(target) == N:
        if check(target):
            #print(answer) 
            if answer == None:
                answer = ''.join([str(i) for i in target])
            return
    
    if cnt == N:
        return

    for i in range(4,7):
        if answer is None:
            target.append(i)
            solve(cnt+1)
            target.pop()

solve(0)
print(answer)