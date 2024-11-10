import heapq
#heappush heappop
import sys

left = []
right = []

inputs = sys.stdin.read().strip().split("\n")
N = int(inputs[0])

for i in range(N):
    num = int(inputs[i+1])
    if num > 0:
        heapq.heappush(right, num)
    elif num < 0:
        heapq.heappush(left, -num)
    else:
        #둘다 원소가 존재할 때
        if left and right:
            l = -heapq.heappop(left)
            r = heapq.heappop(right)
            if r < l:
                print(r)
                heapq.heappush(left, -l)
            else:
                print(l)
                heapq.heappush(right, r)
        #l 에만 원소가 존재할 때
        elif left:
            l = -heapq.heappop(left)
            print(l)
        
        elif right:
            r = heapq.heappop(right)
            print(r)
        else:
            print(0)