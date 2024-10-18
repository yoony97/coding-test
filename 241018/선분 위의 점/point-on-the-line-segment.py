# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


# target보다 큰 최초의 위치를 반환합니다.
def upper_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx


# target보다 같거나 큰 최초의 위치를 반환합니다.
def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx


# 이진탐색을 진행하기 전에
# 정렬을 진행해줍니다.
arr.sort()

# m개의 질의에 대한 답을 계산합니다.
for _ in range(m):
    a, b = tuple(map(int, input().split()))

    # 이진탐색을 진행합니다.
    # b보다 큰 최초의 숫자 위치에서
    # a보다 같거나 큰 최초의 숫자 위치를 빼면
    # 문제에서 원하는 답이 됩니다.
    count = upper_bound(b) - lower_bound(a)
    print(count)