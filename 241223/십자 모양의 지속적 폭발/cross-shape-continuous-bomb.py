n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def boom(i,j, arr):
    rnge = arr[i][j]-1
    for k in range(i-rnge, i+rnge+1):
        if 0 <= k < n:
            arr[k][j] = 0
    for k in range(j-rnge, j+rnge+1):
        if 0 <= k < n:
            arr[i][k] = 0
    return arr

def drop(arr):
    for i in range(n):
        temp =  []
        cnt = 0
        for j in range(n):
            if arr[j][i] != 0:
                temp.append(arr[j][i])
                arr[j][i] = 0
            else:
                cnt += 1
        idx = 0
        for k in range(cnt,n):
            arr[k][i] = temp[idx]
            idx += 1
    return arr

def update(arr):
    n = len(arr)  
    height = [-1] * n  
    
    for j in range(n):
        for i in range(n): 
            if arr[i][j] != 0: 
                height[j] = i  
                break  
    
    return height
height = [0]*n

for _ in range(m):
    op = int(input())
    h = height[op-1]
    arr = boom(h,op-1,arr)
    arr = drop(arr)
    height = update(arr)
    #print(height)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
#print(arr)
