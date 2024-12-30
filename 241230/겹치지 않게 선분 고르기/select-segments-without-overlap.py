N = int(input())
lines = []
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))

def duplicate(point1, point2):
    x1, x2 = point1
    x3, x4 = point2

    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3

    return max(x1, x3) <= min(x2, x4)

def solve(target, selected_count):
    global answer
    if target == N:
        answer = max(selected_count, answer)
        return
    
    # 현재 선분을 선택하지 않는 경우
    solve(target + 1, selected_count)
    
    # 현재 선분을 선택하는 경우
    # 기존에 선택된 선분들과 겹치는지 확인
    valid = True
    for i in range(target):
        if selected[i] and duplicate(lines[target], lines[i]):
            valid = False
            break
    if valid:
        selected[target] = True
        solve(target + 1, selected_count + 1)
        selected[target] = False

# 선택 여부를 저장할 리스트
selected = [False] * N

solve(0, 0)
print(answer)
