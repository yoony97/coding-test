import sys

data = sys.stdin.read().strip().split("\n")
N, G  = map(int, data[0].split())
data = data[1:]
groups = [list(map(int, i.split()[1:])) for i in data]
groups.sort(key = lambda x: (len(x), x[0]))
#print(groups)
s = set([groups[0][0]])
for _ in range(G):
    for i in groups:
        if len(set(i) - s) < 2:
            s = s.union(set(i))    
#        print(s)
print(len(s))