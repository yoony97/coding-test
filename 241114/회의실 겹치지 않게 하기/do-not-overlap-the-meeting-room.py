import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
conf = [tuple(map(int, i.split())) for i in inputs[1:]]
conf.sort(key=lambda x: x[1])

last_time = -1
answer = 0
for (s, e) in conf:
    if s >= last_time:
        answer += 1
        last_time = e
    
print(n-answer)
