n = int(input())
answer = []
visited = [False]*(n+1)
# Write your code here!

def solve(cnt, visited):
    if cnt == n:
        print(" ".join([str(i) for i in answer]))
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            solve(cnt+1, visited)
            answer.pop()
            
            visited[i] = False
            #solve(cnt, visited)

solve(0, visited)