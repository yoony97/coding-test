import sys

data = sys.stdin.read().strip().split("\n")
N = int(data[0])
events = []

for line in data[1:]:
    s, e = map(int, line.strip().split())
    events.append((s, 1))   # 구간 시작: +1
    events.append((e, -1))  # 구간 종료: -1

# 이벤트를 시간 순으로 정렬
# 시간이 같을 경우 시작 이벤트를 먼저 처리하기 위해 두 번째 요소로 정렬
events.sort(key=lambda x: (x[0], x[1]))


current_overlap = 0
max_overlap = 0

for time, change in events:
    current_overlap += change
    if current_overlap > max_overlap:
        max_overlap = current_overlap

print(max_overlap)
