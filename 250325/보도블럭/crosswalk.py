n, L = map(int, input().split())
dist = []
visited = [[0]*n for _ in range(n)]
# Read distance matrix
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    dist.append(row)

def row_solve(arr):
    answer = 0
    for row in arr:
        used = [False]*n
        possible = True
        for i in range(n - 1):
            if row[i] == row[i + 1]:
                continue
            elif row[i] + 1 == row[i + 1]:  # 올라가는 경사로
                for j in range(i, i - L, -1):
                    if j < 0 or row[j] != row[i] or used[j]:
                        possible = False
                        break
                    used[j] = True
            elif row[i] - 1 == row[i + 1]:  # 내려가는 경사로
                for j in range(i + 1, i + 1 + L):
                    if j >= n or row[j] != row[i + 1] or used[j]:
                        possible = False
                        break
                    used[j] = True
            else:
                possible = False
                break
        if possible:
            answer += 1
    return answer


            
dist_t = list(zip(*dist))

print(row_solve(dist_t) + row_solve(dist))


#경사로 설치 조건
#1. 높이 차이가 1이 나는 보도 블럭에 설치 가능, 낮은 칸에 설치됨 3-2 = 2칸에 설치됨
#2. 경사로 길이 L 동안 바닥에 접촉해야함, 경사로가 놓인 보도블럭 높이는 같아야함
#- 한번 끝겼으면 L만큼의 길이가 필요하고, 2번 끊기면 2*L 이 필요함



