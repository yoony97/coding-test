n = int(input())
visited = [False]*(n+1)
answer = []
# Write your code here!


def solve(cur_num):
    if cur_num == n:
        print(' '.join([str(i) for i in answer]))
    
    for i in range(n, 0, -1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            solve(cur_num+1)
            visited[i] = False
            answer.pop()

solve(0)