import sys

N = int(input())
target = []
answer = None

def check(target):
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
                print(answer)
                sys.exit(0)
            return
    
    if cnt == N:
        return

    for i in range(4,7):
        if check(target):
            target.append(i)
            solve(cnt+1)
            target.pop()

solve(0)
