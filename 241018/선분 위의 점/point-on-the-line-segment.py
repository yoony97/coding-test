n, M = map(int, input().split())
arr = list(map(int, input().split()))

def upper_bound(target):
    left = 0                             # 첫 번째 원소의 위치로 설정합니다.
    right = n - 1                        # 마지막 원소의 위치로 설정합니다.
    min_idx = n                          # 최소이므로, 답이 될 수 있는 값보다 더 큰 값으로 설정합니다.

    while left <= right:                 # [left, right]가 유효한 구간이면 계속 수행합니다.
        mid = (left + right) // 2        # 가운데 위치를 선택합니다.
        if arr[mid] > target:           # 만약에 선택한 원소가 target보다 같거나 크다면 
            min_idx = min(min_idx, mid)  # 같거나 큰 값들의 위치 중 최솟값을 계속 갱신해줍니다.
            right = mid - 1              # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        else:
            left = mid + 1               # 작은 경우라면 left를 바꿔줍니다.
    
    return min_idx                       # 조건을 만족하는 최소 index 값을 반환합니다.

def lower_bound(target):
    left = 0                             # 첫 번째 원소의 위치로 설정합니다.
    right = n - 1                        # 마지막 원소의 위치로 설정합니다.
    min_idx = n                          # 최소이므로, 답이 될 수 있는 값보다 더 큰 값으로 설정합니다.

    while left <= right:                 # [left, right]가 유효한 구간이면 계속 수행합니다.
        mid = (left + right) // 2        # 가운데 위치를 선택합니다.
        if arr[mid] >= target:           # 만약에 선택한 원소가 target보다 같거나 크다면 
            min_idx = min(min_idx, mid)  # 같거나 큰 값들의 위치 중 최솟값을 계속 갱신해줍니다.
            right = mid - 1              # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        else:
            left = mid + 1               # 작은 경우라면 left를 바꿔줍니다.
    
    return min_idx                       # 조건을 만족하는 최소 index 값을 반환합니다.




for _ in range(M):
    a, b = map(int, input().split())
    left = lower_bound(a)
    right = lower_bound(b)
    

    print(right - left)