import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
li = [ tuple(map(int, i.split())) for i in inputs[1:] ]
li.sort(key= lambda x: (x[1], x[0]))

answer = 0
end_time = 0
for (s, e) in li:
    if s >= end_time:
        answer += 1
        end_time = e 

print(answer)
