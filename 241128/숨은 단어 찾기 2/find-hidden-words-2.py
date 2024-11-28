N, M = map(int, input().split())
strings = []
# 0: 가로, # 1: 세로 # 2: \ 대각선 # 3: / 대각선
dxs = [1, 0, 1, 1, -1, 0, -1, -1,]
dys = [0, 1, 1, -1, 0, -1, -1, 1]

for i in range(N):
    strings.append(input())
#print(strings)
cnt = 0

for i in range(N):
    for j in range(M):
        for k in range(7):
            string = strings[i][j]
            dx = dxs[k]
            dy = dys[k]
            for l in range(2):
                cx = i + dx
                cy  = j + dy
                if 0 <= cx < N and 0 <= cy < M:
                    string += strings[cx][cy]
            if string == 'LEE':
                cnt += 1

print(cnt//2)