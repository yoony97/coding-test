from collections import deque

def rotate_left(arr, chair):
    temp = arr[chair][0]
    #-1 -> 0, 1-> 0, 2-> 1
    for i in range(7):
        arr[chair][i] = arr[chair][i+1]
    arr[chair][-1] = temp
    
def rotate_right(arr, chair):
    temp = arr[chair][-1]
    for i in range(7, 0,-1):
        arr[chair][i] = arr[chair][i-1]
    arr[chair][0] = temp
    #0 -> 1, 1-> 2,... ,-1 -> 0


#시계가 오른쪽, 반시계가 왼쪽임


arr = []
for i in range(4):
    arr.append(list(map(int, input())))

k = int(input())
op = []
for i in range(k):
    op.append(tuple(map(int, input().split())))

for original, direct in op:
    original -= 1
    direction = [0]*4
    direction[original] = direct
    for i in range(original-1, -1, -1):
        if arr[i][2] != arr[i+1][6]:
            direction[i] = -direction[i+1]
        else:
            break

    for i in range(original+1, 4):
        if arr[i][6] != arr[i-1][2]:
            direction[i] = -direction[i-1]
        else:
            break

    for i in range(4):
        if direction[i] == 1:
            rotate_right(arr, i)
        elif direction[i] == -1:
            rotate_left(arr, i)

answer = 0
for i in range(4):
    answer += (2**i)*arr[i][0]

print(answer)