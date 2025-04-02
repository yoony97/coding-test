#반지름이 r이면 r번째 원판
#각 원판 m개의 정수
#r번째 원판에 적힌 m번째 정수를 (r,m)
#12시부터 m개의 정수가 시계방향 순서대로 주어짐
#독립적으로 원판은 회전함(요청: 종류(x), 방향(d), 칸(k)) #d는 시계 방향 반시계 방향
# x는 원판의 번호가 x의 배수 일 경우 회전
# 인접하고 같은 수면 지움
    # 인접 조건
    # r,1은 r,2와 r,m 과 인접하다 (같은원 좌우 옆에 있는 숫자를 뜻함)
    # r,j는 r-1,j과 r+1,j와 인접하다 (바로 위의 원판과 인접하다)
    # 모듈러로 처리해야할 것 같다.
#원판 숫자가 안지워지는 경우, 숫자가 존재하는 경우
    # 원판 전체에 적힌 수의 평균 구해서 정규화
          # 평균보다 큰 수  N = N-1
          # 평균보다 작은 N = N + 1

from collections import deque
N, M, Q = map(int, input().split())
maps = []
query = []
for i in range(N):
    j = list(map(int, input().split()))    
    maps.append(j) #maps의 index가 maps[r]의 인덱스가 m
    

for i in range(Q):
    x, d, k = map(int, input().split())
    query.append((x,d,k))


#회전하는 함수
def rotate_clock_wise(arr,k):
    for _ in range(k):
        temp = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp


def rotate_counter_clock_wise(arr, k):
    for _ in range(k):
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = temp

def rotate(x, d, k):
    for i in range(N):
        if (i+1)%x == 0:
            if d == 1:
                rotate_counter_clock_wise(maps[i], k)
            else:
                rotate_clock_wise(maps[i], k)




def check():
    visited = [[False]*M for _ in range(N)]
    ismerge = False
    
    for r in range(N):
        for c in range(M):
            if maps[r][c] != 0 and not visited[r][c]:
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                group = [(r, c)]
                target_num = maps[r][c]
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx = x + dx
                        ny = (y + dy) % M  # 좌우 회전 가능성 고려
                        if 0 <= nx < N and not visited[nx][ny] and maps[nx][ny] == target_num:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            group.append((nx, ny))
                
                if len(group) > 1:
                    ismerge = True
                    for x, y in group:
                        maps[x][y] = 0

    return ismerge

def normalize():
    count = 0
    total = 0
    for r in range(N):
        for m in range(M):
            if maps[r][m] != 0:
                count += 1
                total += maps[r][m]
    
    standard = total//count

    for r in range(N):
        for m in range(M):
            if maps[r][m] != 0:
                if maps[r][m] > standard:
                    maps[r][m] -= 1
                if maps[r][m] < standard:
                    maps[r][m] += 1
            
    



def simulate(x, d, k):
    rotate(x, d, k)
    ismerge = check()
    #print(maps)
    if not ismerge:
        normalize()
#    print(maps)

for (x,d,k) in query:
    simulate(x,d,k)



print(sum([sum(maps[i]) for i in range(N)]))







