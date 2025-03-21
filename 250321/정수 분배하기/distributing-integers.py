n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def get_count(mid, arr):
    count = 0
    for num in arr:
        count += num//mid

    return count 

left = 0
right = max(arr)
answer = 0


while left <= right:
    mid = (left+right)//2
    count = get_count(mid, arr)
    if count < m: #좀 더 작게 분해해야한다.
        right = mid - 1
    elif count >= m: #좀 더 크게 분해해도 된다.
        left = mid + 1
        answer = max(answer, mid)

print(answer)
