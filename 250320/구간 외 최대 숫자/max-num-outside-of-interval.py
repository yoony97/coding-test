n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]


for a,b in queries:
    max_value = 0
    left = a-2
    right = b

    while left >= 0:
        max_value = max(arr[left], max_value)
        left -= 1

    while right <= len(arr)-1:
        max_value = max(arr[right], max_value)
        right += 1


    print(max_value)