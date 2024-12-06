N =  int(input())
li = list(map(int,  input().split())) # 숫자가 겹치지 않게 구성된, N개의 수열

def check(li):
    #result = True
    for i in range(1,N):
        if li[i-1] > li[i]:
            return False
    return True

def insert(li, pivot, idx):
    return li[:idx] +[pivot] + li[idx:]
    
cnt = 0
while True:
    #print(li)
    if check(li):
        break

    pivot = li.pop(0)
    target = 0
    for i in range(N-1):
        if li[i] == pivot-1:
            target = i+1
    li = insert(li, pivot, target)
    cnt += 1
print(cnt)
# 선택한 숫자보다 바로 이전 작은 숫자 옆으로 붙이자.

