from collections import deque

chairs = []
for i in range(4):
    chairs.append(list(map(int, [i for i in input()])))
K = int(input())


def rotate_clock(n):
    original = chairs[n]
    temp = original[-1]
    for i in range(7, -1, -1):
        original[i] = original[i-1]

    original[0] = temp
    chairs[n] = original       

def rotate_anti_clock(n):
    original = chairs[n]
    temp = original[0]
    for i in range(7):
        original[i] = original[i+1]
    original[-1] = temp
    chairs[n] = original       
    #0 -> 1, 1->2

for i in range(K):
    cmd = deque([])
    rotated = [False]*4
    n, d = map(int, input().split())
    n -= 1 #0-based
    cmd.append((n, d))
    rotated[n] = True
    while cmd:
        n, d = cmd.popleft()
        #회전하기 전 인접한 테이블구하기
        left = n-1  if n-1 >= 0 else None
        right = n+1 if n+1 < 4 else None

        if left is not None and chairs[left][2] != chairs[n][6] and not rotated[left]:
            cmd.append((left, -1*d))
            rotated[left] = True
        if right is not None and chairs[right][6] != chairs[n][2] and not rotated[right]:
            cmd.append((right, -1*d))
            rotated[right] = True
        
        if d == 1:
            rotate_clock(n)
        else:
            rotate_anti_clock(n)

cnt= 1
answer = 0
for i in range(4):
    answer += cnt*chairs[i][0]
    cnt *= 2

print(answer)


