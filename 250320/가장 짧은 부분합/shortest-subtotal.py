n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
answer = float('inf')
j = 0 
sum_val = 0

for i in range(1, n+1):
    #print(sum_val, end =" ")
    #포인트를 움직이는 조건 1. s에 미만 일때 움직여
    while j < n and sum_val < s:
        sum_val += arr[j]
        j += 1
    if sum_val >= s: 
        answer= min(j-i, answer)
    sum_val -= arr[i]

if answer == float('inf'):
    print(-1)
else:
    print(answer)

# Please write your code here.
