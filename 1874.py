N = int(input())
target = []
for i in range(N):
    s = input()
    target.append(int(s))

def solve(N, target):
    stack = []
    history = []
    number = 1  # 시작 숫자를 1로 초기화

    for value in target:
        while number <= value:  # 필요한 수가 스택의 맨 위에 올 때까지 push
            stack.append(number)
            history.append('+')
            number += 1

        if stack[-1] == value: 
            stack.pop()
            history.append('-')
        else: 
            return ["NO"]

    return history

history = solve(N, target)
for i in history:
    print(i)
    

    




