n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

def solve(dist, history):
    global answer 
    if len(history) == n:
        if A[history[-1]][history[0]] != 0:
            total = dist+ A[history[-1]][history[0]]
            answer = min(answer, total)
        return
    
    for i in range(n):
        if i not in history and A[history[-1]][i] != 0:
            history.append(i)
            solve(dist + A[history[-2]][history[-1]], history)
            history.pop()

    

for start in range(n):
    history = [start]
    solve(0, history)

print(answer)
