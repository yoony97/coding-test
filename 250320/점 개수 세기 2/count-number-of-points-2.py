from sortedcontainers import SortedSet

n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

# (x, y)를 저장하는 정렬된 Set
nums = SortedSet(points)

for (x1, y1, x2, y2) in queries:
    left_idx = nums.bisect_left((x1, float('-inf')))  
    right_idx = nums.bisect_right((x2, float('inf')))  
    count = 0
    for i in range(left_idx, right_idx):
        x, y = nums[i]
        if y1 <= y <= y2:
            count += 1

    print(count)