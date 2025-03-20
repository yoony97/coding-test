n, k = map(int, input().split())
arr = list(map(int, input().split()))
counting_arr = [0]*3
j = 0
ans = float('inf')
for i in range(n):
    while j < n and counting_arr[1] != k:
        counting_arr[arr[j]] += 1
        j+= 1
    
    if counting_arr[1] == k:
        ans = min(ans, j-i)
    
    counting_arr[arr[i]] -= 1
if ans == float('inf'):
    ans = -1

print(ans)
# Please write your code here.
