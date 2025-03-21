def get_sum(n):
    return n*(n+1)//2

s = int(input())
left = 0
right = s
answer = 0
while left <= right:
    mid = (left+right)//2
    if get_sum(mid)  >  s: ## 1부터 mid까지 더한 값이 s 보다 클경우 right를 줄인다.
        right = mid -1
    elif get_sum(mid) < s: 
        answer = max(answer, mid)
        left  = mid + 1
    else:
        answer = mid
        break

print(answer)
        
