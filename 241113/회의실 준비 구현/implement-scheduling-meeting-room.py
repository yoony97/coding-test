import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
li = [ tuple(map(int, i.split())) for i in inputs[1:] ]
li.sort(key= lambda x: (x[1], x[0]))

end = li[-1][1]
flag = [0]*end

answer = 0 
for (s, e) in li:
    if sum(flag[s:e]) == 0:
        answer += 1
        for j in range(s, e):
            flag[j] = 1
        

print(answer)