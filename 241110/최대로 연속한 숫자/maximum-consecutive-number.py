import sys
import threading
import bisect
import heapq
from collections import Counter

sys.setrecursionlimit(1 << 25)
n, m = map(int, sys.stdin.readline().split())
remove_list = list(map(int, sys.stdin.readline().split()))

# Initialize the list of removed numbers with boundaries
removed_numbers = [-1, n+1]
lengths_counter = Counter()
lengths_heap = []

# Initial interval length is the entire range
initial_length = n + 1
lengths_counter[initial_length] += 1
heapq.heappush(lengths_heap, -initial_length)

for x in remove_list:
    # Find position to insert the removed number
    idx = bisect.bisect_left(removed_numbers, x)
    left_neighbor = removed_numbers[idx - 1]
    right_neighbor = removed_numbers[idx]

    # Remove the interval between left_neighbor and right_neighbor
    interval_length = right_neighbor - left_neighbor - 1
    lengths_counter[interval_length] -= 1
    if lengths_counter[interval_length] == 0:
        del lengths_counter[interval_length]

    # Add new intervals created by the removal
    left_interval_length = x - left_neighbor - 1
    if left_interval_length > 0:
        lengths_counter[left_interval_length] += 1
        heapq.heappush(lengths_heap, -left_interval_length)

    right_interval_length = right_neighbor - x - 1
    if right_interval_length > 0:
        lengths_counter[right_interval_length] += 1
        heapq.heappush(lengths_heap, -right_interval_length)

    # Insert the removed number into the sorted list
    removed_numbers.insert(idx, x)

    # Retrieve the current maximum interval length
    while lengths_heap:
        max_length = -lengths_heap[0]
        if lengths_counter.get(max_length, 0) > 0:
            break
        else:
            heapq.heappop(lengths_heap)
    else:
        max_length = 0

    print(max_length)