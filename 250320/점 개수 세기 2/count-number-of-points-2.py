from sortedcontainers import SortedSet

n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]
nums = SortedSet()
maps = {}

for (x,y) in points:
    nums.add((x,y))

idx = 0
for (x,y) in nums:
    maps[str(x)+str(y)] = idx
    idx += 1

#print(maps)

for (x1,y1,x2,y2) in queries:
    left_idx = nums.bisect_left((x1,y1))
    right_idx = nums.bisect_right((x2,y2))
    if left_idx == len(nums) and right_idx == len(nums):
        print(0)
        
    elif left_idx == right_idx-1:
        print(1)
    else:
        lx,ly = nums[left_idx]
        rx,ry = nums[right_idx-1]

        print(maps[str(rx)+str(ry)]- maps[str(lx)+str(ly)])
        
    



    