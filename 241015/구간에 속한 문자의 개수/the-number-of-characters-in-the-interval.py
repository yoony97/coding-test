import sys
import pprint
data = sys.stdin.read().strip().split("\n")
N, M, K = map(int, data[0].split())
data = data[1:]

a_arr = [[0]*(N+1) for _ in range(N+1)]
b_arr = [[0]*(N+1) for _ in range(N+1)]
c_arr = [[0]*(N+1) for _ in range(N+1)]
aS = [[0]*(N+1) for i in range(N+1)]
bS = [[0]*(N+1) for i in range(N+1)]
cS = [[0]*(N+1) for i in range(N+1)]
#init
for i in range(N):
    s = data[i]
    for j in range(M):
        if s[j] == 'a':
            a_arr[i+1][j+1] = 1
        if s[j] == 'b':
            b_arr[i+1][j+1] = 1
        if s[j] == 'c':
            c_arr[i+1][j+1] = 1

data = data[N:]

#make prefix

for i in range(1, N+1):
    for j in range(1, N+1):
        aS[i][j] = aS[i-1][j] + aS[i][j-1] - aS[i-1][j-1] +a_arr[i][j] 
        bS[i][j] = bS[i-1][j] + bS[i][j-1] - bS[i-1][j-1] +b_arr[i][j] 
        cS[i][j] = cS[i-1][j] + cS[i][j-1] - cS[i-1][j-1] +c_arr[i][j] 

def get_sum(S, x1, y1, x2, y2):
    return S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]



for i in data:
    x1,y1,x2,y2 = map(int, i.split())
    #x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2 -1
    print(get_sum(aS, x1,y1,x2,y2), get_sum(bS, x1,y1,x2,y2), get_sum(cS, x1,y1,x2,y2))