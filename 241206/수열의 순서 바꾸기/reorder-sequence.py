N =  int(input())
li = list(map(int,  input().split())) # 숫자가 겹치지 않게 구성된, N개의 수열
    
cnt = 1  # 현재 증가 부분 수열 길이
LIS = 1  # 최대 LIS 길이 저장

for i in range(1, N):
    if li[i] > li[i-1]:
        cnt += 1
    else:
        LIS = max(LIS, cnt)
        cnt = 1  

LIS = max(LIS, cnt)  

print(N-LIS )