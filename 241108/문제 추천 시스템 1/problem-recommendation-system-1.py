import sys
from sortedcontainers import SortedSet
s = SortedSet()
#s = SortedSet()
dic = dict()
data = sys.stdin.read().strip().split("\n")
n = int(data[0])
for i in range(n):
    p, l = map(int, data[i+1].split())
    if l in dic.keys():
        dic[l].add(p)
    else: 
        dic[l] = set([p])
    s.add((l,p))

k = int(data[n+1])
inputs_op = data[n+2:]

for i in range(k):
    ops = inputs_op[i].split()
    if ops[0] == 'ad':
        p, l = int(ops[1]), int(ops[2])
        if l in dic: 
            dic[l].add(p)
        else:
            dic[l] = set([p])
        s.add((l, p))
        
    if ops[0] == 'sv':
        p, l = int(ops[1]), int(ops[2])
        dic[l].remove(p)
        s.remove((l, p))
    
    if ops[0] == 'rc':
        #가장 낮은 번호, 문제 번호 작은거
        if int(ops[1]) == -1:
            tl = s[0][0]
            print(min(dic[tl]))
        #가장 높은 번호, 문제 번호 작은거
        if int(ops[1]) == 1:
            tl = s[-1][0]
            print(max(dic[tl]))