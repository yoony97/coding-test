#덧셈 뺼셈 곱셈
#연산자간의 우선순위 무시
#차례대로 계산함


minimum = float('inf')
maximum = float('-inf')

n = int(input())
numbers = list(map(int, input().split()))
count = list(map(int, input().split())) #[덧셈, 뺄샘, 곱셈] 개수

def back(idx, value, plus, minus, mul):
    global minimum, maximum
    if idx == n:
        minimum = min(minimum, value)
        maximum = max(maximum, value)
        return

    if plus:
        back(idx + 1, value + numbers[idx], plus - 1, minus, mul)
    if minus:
        back(idx + 1, value - numbers[idx], plus, minus - 1, mul)
    if mul:
        back(idx + 1, value * numbers[idx], plus, minus, mul - 1)

# 시작은 numbers[0], idx = 1부터 시작
back(1, numbers[0], count[0], count[1], count[2])
        

print(minimum, maximum)