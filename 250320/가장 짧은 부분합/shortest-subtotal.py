n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = float('inf')


for i in range(n):
    j = i
    temp = arr[i]
    while j < n and temp <= s:
        temp += arr[j]
        j += 1

    answer= min(j-i+1, answer)

print(answer)    

# Please write your code here.
