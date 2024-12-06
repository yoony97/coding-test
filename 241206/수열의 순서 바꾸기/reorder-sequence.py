N = int(input())
li = list(map(int, input().split()))
cnt = 0
for i in range(N):
    flag = False
#while not check(li, target):
    for j in range(i, N-1):
        if li[j] > li[j+1]:
            flag = True
    if flag:
        cnt += 1    

print(cnt)