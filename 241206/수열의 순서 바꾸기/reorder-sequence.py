N =  int(input())
li = list(map(int,  input().split())) # 숫자가 겹치지 않게 구성된, N개의 수열
    
max_length = 1  
current_length = 1 

for i in range(1, len(li)):
    if li[i] - li[i-1] == 1:
        current_length += 1
    else:
        max_length = max(max_length, current_length) 
        current_length = 1


max_length = max(max_length, current_length)
print(N-max_length)