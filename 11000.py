import sys

data = sys.stdin.read().strip().split('\n')
N = int(data[0])
li = []
max_time = 0
for i in data[1:]:
    s, e = map(int, i.split())
    li.append((s, 1))
    li.append((e, -1))



li.sort(key = lambda x: (x[0], x[1]))

current_overlap = 0
max_overlap = 0

print(li)
for time, change in li:
    current_overlap += change
    if current_overlap > max_overlap:
        max_overlap = current_overlap

print(max_overlap)
