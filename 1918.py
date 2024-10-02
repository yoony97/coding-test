expression = input()

precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
stack = []
output = ''
for s in expression:
    if s.isalpha():  # 피연산자 처리
        output += s
    elif s == '(':   # 왼쪽 괄호는 스택에 푸시
        stack.append(s)
    elif s == ')':   # 오른쪽 괄호는 '('를 만날 때까지 스택에서 팝
        while stack and stack[-1] != '(':
            output += stack.pop()
        stack.pop()  # '(' 제거
    elif s in precedence:  # 연산자 처리
        while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[s]:
            output += stack.pop()
        stack.append(s)
# 스택에 남은 연산자 모두 출력
while stack:
    output += stack.pop()
print(output)
