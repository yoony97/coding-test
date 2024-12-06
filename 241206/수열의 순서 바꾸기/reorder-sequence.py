N =  int(input())
li = list(map(int,  input().split())) # 숫자가 겹치지 않게 구성된, N개의 수열
target_li = list(range(1,N+1))
def check(li):
    results = []
    #checked = True
    for i, j in zip(li, target_li):
        if i == j:
            results.append(True)
        else:
            results.append(False)
            #checked = False
    return results

def insert(li, pivot, idx):
    return li[:idx] +[pivot] + li[idx:]
    
results = check(li)
LIS = 0
cnt = 0
for i in results:
    if i:
        cnt += 1
    else:
        LIS = max(LIS, cnt)
        cnt = 0

print(N-LIS+1)
    

# 선택한 숫자보다 바로 이전 작은 숫자 옆으로 붙이자.
# 맨 뒤로 보내는 경우의 수는 li[0] == N 일 때, 맨 뒤로 보낸다.
#
# 1 2 3 5 4 6
# 2 3 5 1 4 6
# 3 5 1 2 4 6
# 5 1 2 3 4 6
# 1 2 3 4 5 6
