import sys
from collections import deque


data = sys.stdin.read().strip().split("\n")
R, C = map(int, data[0].split()) # 세로 $R$칸, 가로  $C$칸
table = [i for i in data[1:]]
visited = [[False]*C for _ in range(R)]
q = deque([[(0,0),table[0][0]]])
visited[0][0] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

stack = [[(0,0),table[0][0]]]

    
while stack:
    (cx, cy), history = stack.pop()
    if len(history) > answer:
        answer = len(history)

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] not in history:
            if not visited[nx][ny]:
                stack.append([(nx,ny), history + table[nx][ny]])


print(answer)


# # BFS
# while q:
#     (cx, cy), history = q.popleft()
#     if len(history) > answer:
#         answer = len(history)
    
#     if len(history) < answer:
#         continue
    
#     for i in range(4):
#         nx = cx + dx[i]
#         ny = cy + dy[i]
#         if 0 <= nx < R and 0 <= ny < C and table[nx][ny] not in history:
#             if not visited[nx][ny]:
#                 q.append([(nx,ny), history + table[nx][ny]])

# print(answer)



