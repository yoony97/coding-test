from sortedcontainers import SortedDict
n = int(input())
li = list(map(int, input().split()))
d = SortedDict()

for i in range(n):
    if li[i] not in d:
        d[li[i]] = i+1
    

for key in d:
    print(f"{key} {d[key]}")