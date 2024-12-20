

N, M, Q = map(int, input().split())
arr = []
ops = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(Q):
    ops.append(list(map(int,input().split())))
    #r1, c2, r2, c2 # 1-index

def rshift(op):
    r1, c1, r2, c2 = [i-1 for i in op]
    temp = arr[r1][c2]
    for i in range(c2, c1, -1):
        arr[r1][i] = arr[r1][i-1]

    return temp

def downshift(op, value):
    r1, c1, r2, c2 = [i-1 for i in op]
    temp = arr[r2][c2]
    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i-1][c2]
    arr[r1+1][c2] = value

    return temp

def lshift(op, value):
    r1, c1, r2, c2 = [i-1 for i in op]
    temp = arr[r2][c1]
    for i in range(c1, c2):
        arr[r2][i] = arr[r2][i+1]
    arr[r2][c2-1] = value
    return temp

def upshift(op, value):
    r1, c1, r2, c2 = [i-1 for i in op]
    for i in range(r1, r2):
        arr[i][c1] = arr[i+1][c1]
    arr[r2-1][c1] = value


def rotate(op):
    value = rshift(ops[0])
    value = downshift(ops[0], value)
    value = lshift(ops[0], value)
    upshift(ops[0], value)

def means(op): 
    copyed = [[arr[i][j] for j in range(M)] for i in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    r1, c1, r2, c2 = [i-1 for i in op]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            s = arr[i][j]
            cnt = 1
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    s += arr[nx][ny]
                    cnt += 1 
            copyed[i][j] = s//cnt

    return copyed
    


def pprint(arr):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end =' ')
        print()
    print()
for op in ops:
    rotate(op)
    arr = means(op)
pprint(arr)

