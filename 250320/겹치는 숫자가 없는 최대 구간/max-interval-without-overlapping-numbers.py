n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
counting_arr = [0]*(100001)
j = 0
answer = 0
for i in range(1,n+1):
    while j+1 <= n and counting_arr[arr[j+1]] == 0 :
        counting_arr[arr[j+1]] += 1
        j+= 1
    
    answer = max(answer, j-i+1)

    counting_arr[arr[i]] -= 1

print(answer)
# Please write your code here.
