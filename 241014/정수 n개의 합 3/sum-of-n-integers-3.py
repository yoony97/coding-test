n, k = map(int, input().split())
maps = [[0]*(n+1)]
for i in range(n):
    maps.append([0] + list(map(int, input().split())))

prefix = [[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j] - prefix[i-1][j-1] + maps[i][j]

def get_sum(x1,y1,x2,y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1 -1] + prefix[x1 -1 ][y1-1]

answer = 0 
for i in range(1, n-k +2):
    for j in range(1, n-k+2):
        answer = max(answer, get_sum(i, j, i+k -1 , j+k-1))

print(answer)