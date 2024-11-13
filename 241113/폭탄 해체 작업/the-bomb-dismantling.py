import sys

inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
li = [tuple(map(int, i.split())) for i in inputs[1:]]
times = set()

li.sort(key= lambda x: x[0], reverse=True)
print(li)
answer = 0
for (score, time) in li:
    if time not in times:
        times.add(time)
        answer += score

print(answer)