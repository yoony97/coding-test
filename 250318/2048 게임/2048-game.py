#움직이는 함수
#합치는 함수
#다시 정렬하는 함수

N = int(input())
maps = []
for _ in range(N):
    inputs = list(map(int, input().split()))
    maps.append(inputs)

def up(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for _ in range(n):
        for col in range(n):
            for row in range(n-1):
                if new_arr[row][col] == 0:
                    new_arr[row][col] = new_arr[row+1][col]
                    new_arr[row+1][col] = 0 
    
    return new_arr

def down(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for _ in range(n):
        for col in range(n):
            for row in range(n-1, 0, -1):
                if new_arr[row][col] == 0:
                    new_arr[row][col] = new_arr[row-1][col]
                    new_arr[row-1][col] = 0 

    return new_arr

def left(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for _ in range(n):
        for row in range(n):
            for col in range(0, n-1):
                if new_arr[row][col] == 0:
                    new_arr[row][col] = new_arr[row][col+1]
                    new_arr[row][col+1] = 0 

    return new_arr

def right(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for _ in range(n):
        for row in range(n):
            for col in range(n-1, 0, -1):
                if new_arr[row][col] == 0:
                    new_arr[row][col] = new_arr[row][col-1]
                    new_arr[row][col-1] = 0 

    return new_arr

def check_up(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for col in range(n):
        for row in range(n-1):
            if new_arr[row][col] == new_arr[row+1][col]:
                new_arr[row][col] = new_arr[row][col]*2
                new_arr[row+1][col] = 0
    return new_arr

def check_down(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for col in range(n):
        for row in range(n-1, 0, -1):
            if new_arr[row][col] == new_arr[row-1][col]:
                new_arr[row][col] = new_arr[row][col]*2
                new_arr[row-1][col] = 0
    return new_arr


def check_right(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for row in range(n):
        for col in range(n-1, 0, -1):
            if new_arr[row][col] == new_arr[row][col-1]:
                new_arr[row][col] = new_arr[row][col]*2
                new_arr[row][col-1] = 0
    return new_arr

def check_left(arr):
    n = len(arr)
    new_arr = [[ i for i in arr[j]] for j in range(N)]
    for row in range(n):
        for col in range(n-1):
            if new_arr[row][col] == new_arr[row][col+1]:
                new_arr[row][col] = new_arr[row][col]*2
                new_arr[row][col+1] = 0
    return new_arr


def simulation(arr, direct):
    if direct == 0:
        new_arr = up(arr)
        new_arr = check_up(new_arr)
        new_arr = up(new_arr)

    if direct == 1:
        new_arr = down(arr)
        new_arr = check_down(new_arr)
        new_arr = down(new_arr)
    
    if direct == 2:
        new_arr = left(arr)
        new_arr = check_left(new_arr)
        new_arr = left(new_arr)
    
    if direct == 3:
        new_arr = right(arr)
        new_arr = check_right(new_arr)
        new_arr = right(new_arr)
    
    return new_arr
    
#백트래킹 해야할듯?
#백트레킹 어떻게 할래?
#백트레킹 할려면, 아래처럼 결국 넣었다가 진행하고, 빼고
# up up up up up -> up up up up left 
#그럴려면 어떤 방법이 적합할까?
#4^5 * O(n^3)가 시간 복잡도네? 
#1024만큼 재귀 돌려야하긴해
answer = 0

def backtracking(hist):
    global answer 
    global maps
    if len(hist) == 5:
        new_arr = [[ i for i in maps[j]] for j in range(N)]
        for i in hist:
            new_arr = simulation(new_arr, i)
        answer = max(answer, max([max(i) for i in new_arr]))
        return
    else:
        for i in range(4):
            hist.append(i)
            backtracking(hist)
            hist.pop()


backtracking([])
print(answer)
