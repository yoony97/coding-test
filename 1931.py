import sys
from queue import deque
input = sys.stdin.read
data = input().strip().split("\n")
N = int(data[0])
element = data[1:]
meetings = []

for i in element:
    s,e = map(int, i.split())
    meetings.append((s,e))

# 회의를 끝나는 시간 순으로 정렬, 끝나는 시간이 같다면 시작 시간 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

last_end_time = 0
count = 0

for start, end in meetings:
    if start >= last_end_time:
        last_end_time = end
        count += 1

print(count)
        
    
    

