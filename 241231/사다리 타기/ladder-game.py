from collections import deque

n, m = map(int, input().split())
lines = deque([])
selected = deque([])
answer = float('inf')

for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a,b))

def play(lines, start):
    length = len(lines)
    current = start
    for i in range(length):
        a, b = lines[i]
        if current == a:
            current = a+1
        elif current == a+1:
            current = a            
    return current


def simulate(lines):
    result = []
    lines = list(lines)
    lines.sort(key= lambda x: x[1])
    for i in range(1, n+1):
        dest = play(lines, i)
        result.append(dest)
    return ''.join([str(j) for j in result])


def solve(cnt, target):
    global answer
    
    if cnt == m:
        if target == simulate(selected):
            answer = min(answer, len(selected))
        return
    
    selected.append(lines[cnt])
    solve(cnt + 1, target)
    selected.pop()
    solve(cnt + 1, target)

target = simulate(lines)
solve(0, target)
print(answer)