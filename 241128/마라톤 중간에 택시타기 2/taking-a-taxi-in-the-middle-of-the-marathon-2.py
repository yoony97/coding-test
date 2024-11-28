#1번 N번 제외 체크포인트 건너 뛰기
#한개 건너뛰면 최소 거리 몇?
N = int(input())
cp = []
for i in range(N):
    a, b= map(int, input().split())
    cp.append((a,b))
start = (0,0)

def distance(li):
    dist = 0
    for i in range(1, N-1):
        dist += abs(li[i-1][0] - li[i][0]) + abs(li[i-1][1] - li[i][1])
    return dist
ans = float('inf')
for i in range(2,N):
    #print(cp[:i-1] + cp[i:])
    dis = distance(cp[:i-1] + cp[i:])
    ans = min(ans, dis)
print(ans)