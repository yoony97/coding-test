expression = input().strip()

answer = float('-inf')
var_mapping = {}  # 'a'~'f'를 1~4 사이 값으로 매핑

# 백트래킹을 통해 'a'~'f'를 1~4 값으로 할당
def assign_variables(used_vars):
    if len(used_vars) == len(set(c for c in expression if 'a' <= c <= 'f')):  # 모든 문자에 대해 할당 완료
        solve(0, 0, None)
        return

    var = list(set(c for c in expression if 'a' <= c <= 'f'))[len(used_vars)]  # 할당할 변수 선택

    for num in range(1, 5):  # 1~4 중 선택
        var_mapping[var] = num
        assign_variables(used_vars + [var])
        del var_mapping[var]  # 백트래킹 (원상 복구)

# 연산 수행 함수
def solve(idx, current, prev):
    global answer
    if idx == len(expression):
        answer = max(answer, current)
        return

    if 'a' <= expression[idx] <= 'f':  # 변수인 경우
        cur_num = var_mapping[expression[idx]]  # 매핑된 숫자 가져오기
        
        if prev is None:
            solve(idx + 1, cur_num, prev)
        else:
            if prev == '+':
                solve(idx + 1, current + cur_num, prev)
            elif prev == '-':
                solve(idx + 1, current - cur_num, prev)
            elif prev == '*':
                solve(idx + 1, current * cur_num, prev)
    else:
        solve(idx + 1, current, expression[idx])  # 연산자 저장 후 진행

assign_variables([])  # 백트래킹 시작
print(answer)
