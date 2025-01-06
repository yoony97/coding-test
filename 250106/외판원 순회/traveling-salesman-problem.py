n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

def solve(cur, dist, history):
    global answer 
    if len(history) == n:
        answer = min(answer, dist+ A[history[-1]][history[0]])
        return
    
    for i in range(n):
        if i not in history:
            history.append(i)
            solve(cur+1, dist + A[history[-2]][history[-1]], history)
            history.pop()

    

for start in range(n):
    history = [start]
    solve(0, 0, history)

print(answer)