# 모든 자리에 대해 첫 번째 조합과 거리가 2 이내이거나,
# 모든 자리에 대해 두 번째 조합과 거리가 2 이내에 있으면 열리게 됩니다.
N = int(input())
a1,b1,c1 = list(map(int, input().split()))
a2,b2,c2 = list(map(int, input().split()))
li = set()

def isclosed(i,a):
    if abs(i - a) >= N-2 or 0 <=  abs(i - a) <= 2:
        return True
    return False
    
    
def check(a,b,c,i,j,k):
    if isclosed(i, a) and isclosed(j,b) and isclosed(k,c):
        return True
    return False
    
cnt = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if check(a1,b1,c1,i,j,k) or check(a2,b2,c2,i,j,k):
                li.add((i,j,k))
#print(li)
print(len(li))
#2 - 2  + 9 % 10 
 